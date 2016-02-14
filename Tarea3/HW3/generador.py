__author__ = 'sharop'

# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
import string, numpy, getopt, sys, random, time, re, pprint, codecs, json
from jsonl import jsonl

from pprint import pprint

data =[]
with codecs.open('corpus_entrenamiento.jsonline') as f:
    for line in f:
        data.append(json.loads(line))

