#!/usr/bin/env python3
import csv
import sys
from xml.etree.ElementTree import Element, SubElement, ElementTree

#
# Based on Specification
# http://xml.coverpages.org/tmxSpec971212.html
#

# initial configuration
src = 'en'
variants = ['pt','pt-BR', 'pt-PT']
# possible status 'provisional','approved','non-standard','forbidden','rejected','obsolete'
acceptedStatus = ['provisional', 'approved', '']
fieldnames = ['src:en', 'src:pos', 'tgt:pt', 'term status:pt', 'comment:pt', 'tgt:pt-BR', 'term status:pt-BR', 'comment:pt-BR',
              'tgt:pt-PT', 'term status:pt-PT', 'comment:pt-PT', 'tgt:pt-AO', 'term status:pt-AO', 'comment:pt-AO', 'concept id']

# create XML root and header
root = Element('tmx')
root.set('version', '1.4')
header = SubElement(root, 'header')
header.set('creationtool', 'utx2xml')
header.set('creationtoolversion', 'beta')
header.set('datatype', 'PlainText')
header.set('segtype', 'sentence')
header.set('adminlang', 'en-us')
header.set('srclang', src)
header.set('o-tmf', 'ABCTransMem')

body = SubElement(root, 'body')

csv.register_dialect('utx', delimiter='\t',
                     quoting=csv.QUOTE_NONE, lineterminator='\r\n')

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

        # create an entry
        tu = SubElement(body, 'tu')

        # add variation in original language
        tuv = SubElement(tu, 'tuv')
        tuv.set('xml:lang', src)
        seg = SubElement(tuv, 'seg')
        seg.text = entry['src:'+src]

        # add variatios to destination languages
        for variant in variants:
            # validate the status of the translation
            if not entry['term status:'+variant] in acceptedStatus:
                continue
            
            # if translation field is empty, skip
            if entry['tgt:'+variant] == '':
                continue

            tuv = SubElement(tu, 'tuv')
            tuv.set('xml:lang', variant)
            seg = SubElement(tuv, 'seg')
            seg.text = entry['tgt:' + variant]

        # remove tu if there is not translation
        if len(list(tu)) <= 1:
            body.remove(tu)

    # ElementTree(root).write('output.tmx', encoding='utf-8')
    ElementTree(root).write('../ficheiros/Dicionario.tmx', encoding='utf-8')
