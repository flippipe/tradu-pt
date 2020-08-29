# Memória de Tradução
Visto não ter encontrado nenhuma memória de tradução que podesse ser facilmente utilizável ou completa, recorri à ideia do Julinao de ter como base [Glossário da Sociedade da Informação](https://apdsi.pt/glossario/) e com base nessa informação criar uma memória de tradução comunitária, para todos que traduzimos para Português possamos ter uma base comum.

Pensei converter o PDF para o formato [TMX](https://en.wikipedia.org/wiki/Translation_Memory_eXchange) para usar com o POEdit, mas seria dificil em comunidade manter esse formato ou alguma informação extra.

Entretanto descobri que o [UTX](https://aamt.info/english/about/) poderá ser uma boa forma de cooperar-mos, permite ser multi lingua e facil processamento se quisermos criar programas que converta o UTX e TMX ou outro formato.

## UTX

- Simples - podemos usar um editor de texto (não recomendo), mas pode ser gerido numa simples folha de cálculo ou colocar numa folha de cálculo online para todos editarmos.
- Multilingual - podemos lá colocar as traduções dos diversos "portugueses" existentes, e cada tradução pode ter o seu estado ou comentário.
- Convertível - como é um formato simples, é de fácil processamento para converter noutros formatos.

### Informação que é possível ter

- pos - indicação da parte do discurso, ie, se é nome, verbo, adjectivo etc etc
- estado - a especificação permite ter a tradução em diversos estados, como por exemplo, aprovado, proposto, proibido
- comentário
    
Toda esta informação, num único documento, para as diversas variações de português.


### Exemplo

Podem encontrar um primeiro esboço desse documento [aqui](https://github.com/flippipe/tradu-pt/ficheiros/Dicionario.utx.tsv) no Github, na diretoria ficheiros, mas segue um pequeno exemplo:

|src:en|src:pos|tgt:pt|term status:pt|comment:pt|tgt:pt-BR|term status:pt-BR|comment:pt-BR|tgt:pt-PT|term status:pt-PT|comment:pt-PT|tgt:pt-AO|term status:pt-AO|comment:pt-AO|concept id|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|backdoor|noun|porta de serviço|rejected||||||||||||
|spreadsheet|noun|folha de cálculo|aproved||planilha|aproved|||||||||
|Excel|noun|Excel|non-standard||||||||||||
|e­mail|noun|correio eletrónico|aproved||correio eletrônico|aproved|||||||||


### Variações

Apesar do Português ser o nome da língua oficial, as variações geográficas (ex: pt-pt vr pt-br) ou temporais (com ou sem acordo ortográfico) acontecem.

O ficheiro com criado com a seguinte ideia em mente. Os termos em PT, serão usados se não existir uma variação mais especifica e caso existam diversas traduções, a maioritária nas diversas versões.

Depois temos as duas grandes variações (que conheço), que é o Português da América (pt-BR) Latina e o Português da Europa (pt-PT).

Para finalizar, quem quizer fazer uma tradução de acordo com o Acordo Ortográfico, pedimos emprestado à Comunidade Angolana o a sua variação (pt-AO).

#### Lista completa

- Portuguese (Angola) (pt_AO)
- Brazilian Portuguese (pt_BR)
- Portuguese (Switzerland) (pt_CH)
- Portuguese (Cape Verde) (pt_CV)
- Portuguese (Equatorial Guinea) (pt_GQ)
- Portuguese (Guinea-Bissau) (pt_GW)
- Portuguese (Luxembourg) (pt_LU)
- Portuguese (Macau SAR China) (pt_MO)
- Portuguese (Mozambique) (pt_MZ)
- European Portuguese (pt_PT)
- Portuguese (São Tomé & Príncipe) (pt_ST)
- Portuguese (Timor-Leste) (pt_TL)

(sei que os locales não representam as línguas, mas pelo menos serve de referência)

[fonte](https://www.localeplanet.com/icu/pt/index.html)

### Mais fontes de informação

* [Memória Tradução Ubuntu](https://wiki.ubuntu.com/PortugalTeam/TranslationMemory)
* [Wikipedia - Guia Tradução](https://pt.wikipedia.org/wiki/Ajuda:Guia_de_tradu%C3%A7%C3%A3o/Lista_de_termos_t%C3%A9cnicos_de_inform%C3%A1tica)
* [Glossário Inglês-Português de Informática](https://quark.fe.up.pt/cgi-bin/orca/glossario)

### Software

* [Wikipedia - translation software](https://en.wikipedia.org/wiki/List_of_translation_software)
* [utx2tmx.py](https://github.com/flippipe/tradu-pt/blob/master/scripts/utx2tmx.py) Script rudimentar para transformar conteúdo do UTX para TMX
* [utx2po.py](https://github.com/flippipe/tradu-pt/blob/master/scripts/utx2po.py) Script rudimentar para transformar conteúdo do UTX para PO