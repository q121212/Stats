#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import string
frequency = {}
with open('text.txt', 'r', encoding='utf8') as document_text:
  text_string = document_text.read().lower()
  match_pattern = re.findall(r'\w{2,15}', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 

for word in frequency_list:
    print(word, frequency[word])