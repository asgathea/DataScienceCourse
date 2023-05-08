#!/usr/bin/python
# -*- coding: utf-8 -*-

# run: python3 lettercount.py text

import sys, re

def count_letter(userInput):
	letterDict = {}

	for i in userInput:
		if i not in letterDict:
			if re.match('[a-zA-Z]', i):
				letterDict[i] = 1
			elif re.match('\d', i):
				raise ValueError('No digits, please!')
		else:
			letterDict[i] = letterDict[i] + 1

	print(letterDict)

count_letter(sys.argv[1])