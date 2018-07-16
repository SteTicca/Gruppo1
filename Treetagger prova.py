# encoding: utf-8

from __future__ import unicode_literals

import treetaggerwrapper
from treetaggerwrapper import *
import pprint

tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')

tags = tagger.tag_text("Questo è un testo veramente corto da taggare.")

pprint.pprint(tags)

tags2 = treetaggerwrapper.make_tags(tags)

pprint.pprint(tags2)

filein = "./hash_text.txt"
fileout = "./hash_tags.txt"

tagger.tag_file_to(filein,fileout, encoding="utf-8")
