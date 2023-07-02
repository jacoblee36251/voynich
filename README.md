# Voynich Manuscript Parser and Resources
Pure Python parser for the [IVTFF](http://www.voynich.nu/software/ivtt/IVTFF_format.pdf)-formatted [ZL transliteration](http://www.voynich.nu/data/ZL_ivtff_1r.txt) of the [Voynich Manuscript](https://en.wikipedia.org/wiki/Voynich_manuscript).

Intended for NLP/ML/DL use on the Voynich Manuscript.

## Installation

`pip install voynich`

[PyPi page](https://pypi.org/project/voynich/)

## Example Usage

`voynich.VoynichManuscript` is what you'll likely mostly be using, it contains `voynich.Page`s, which contain `voynich.Line`s.

Example usage (subject to change):

```Python
>>> from voynich import VoynichManuscript

>>> vm = VoynichManuscript(path_to_txt, inline_comments=False)

>>> print(vm)
VoynichManuscript(num_pages=227, inline_comments=False)

>>> print(vm.pages["f1r"])
Page(page_name=f1r, quire_num=None, folio_num=None, num_lines=31, illust_type=None)

>>> print(vm.pages["f1r"][0])
Line(<%>fachys.ykal.ar.ataiin.shol.shory.[cth:oto]res.y.kor.sholdy)

>>> print(vm.pages["f1r"][0].text)
<%>fachys.ykal.ar.ataiin.shol.shory.[cth:oto]res.y.kor.sholdy

>>> print(vm.get_paragraphs()[0])
'fachys.ykal.ar.ataiin.shol.shory.cthres.y.kor.sholdy.sory.ckhar.or,y.kair.chtaiin.shar.ase.cthar.cthar,dansyaiir.sheky.or.ykaiin.shod.cthoary.cthes.daraiin.sysoiin.oteey.oteos,roloty.cthiar,daiin.okaiin.or.okansair,y.chear.cthaiin.cphar.cfhaiinydaraishy'
```

Each `Page` object also contains a list of paragraphs `Page.paragraphs`. These paragraphs have some additional processing on them, removing paragraph markers (`<%>` and `<$>`), gap indicators (`<->`), and (currently) chooses the first possible interpretation of ambiguous characters (i.e. `[o:a]` -> `o`). For future work, will update paragraph parser to produce one paragraph for every possible combination of ambiguous characters.
