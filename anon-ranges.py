#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create list which can be used in https://github.com/edsu/anon
# Строит список, который можно использовать в https://github.com/edsu/anon
import json

def generate(filename,lang):
  ranges = {'ranges':{}}
  with open(filename) as f:
    jsonranges = json.load(f)
    for entry in jsonranges:
      ranges['ranges'][entry['name'][lang]['short']] = entry['ranges']
    print json.dumps(ranges, ensure_ascii = False, sort_keys=True, indent=2, separators=(',', ': '))

generate('ranges.json','uk')
generate('ranges.json','ru')
generate('ranges.json','en')
