#!/usr/bin/env python3
import csv

# initial configuration
src = 'en'
variants = ['pt-BR','pt','pt-PT'] # will try to find a match from begin of the list, latest win
# possible status 'provisional','approved','non-standard','forbidden','rejected','obsolete'
acceptedStatus = ['provisional', 'approved', '']
fieldnames = ['src:en', 'src:pos', 'tgt:pt', 'term status:pt', 'comment:pt', 'tgt:pt-BR', 'term status:pt-BR', 'comment:pt-BR',
              'tgt:pt-PT', 'term status:pt-PT', 'comment:pt-PT', 'tgt:pt-AO', 'term status:pt-AO', 'comment:pt-AO', 'concept id']

csv.register_dialect('utx', delimiter='\t',
                     quoting=csv.QUOTE_NONE, lineterminator='\r\n')

dicionary={}
with open('../ficheiros/Dicionario.utx.tsv') as f:
    reader = csv.DictReader(f, fieldnames, dialect='utx')
    next(reader, None)  # skip the headers
    next(reader, None)
    next(reader, None)
    for entry in reader:
        # print (entry)

        # skip if original term is not present
        if entry['src:'+src] is None:
            continue

        translatedString=''
        for variant in variants:
            # validate the status of the translation
            if not entry['term status:'+variant] in acceptedStatus:
                continue
            
            # if translation field is empty, skip
            if entry['tgt:'+variant] == '':
                continue

            translatedString=entry['tgt:'+variant]

        # skip if no translations was found
        if translatedString == '':
            continue
        
        dicionary[entry['src:'+src]]=translatedString

# write to disk
poFile = open('../ficheiros/Dicionario.po', 'w')
for original, translated in dicionary.items():
    poFile.write('msgid "{}"\nmsgstr "{}"\n\n'.format(original, translated)) 
poFile.close()