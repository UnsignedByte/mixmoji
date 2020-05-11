# -*- coding: utf-8 -*-
# @Author: UnsignedByte
# @Date:   00:57:21, 11-May-2020
# @Last Modified by:   UnsignedByte
# @Last Modified time: 02:44:13, 11-May-2020

from io import BytesIO
import cairosvg
from PIL import Image
import re

def readSVG(path, scale=40):
	out = BytesIO()
	cairosvg.svg2png(url=path, write_to=out,scale=scale)
	return Image.open(out) 

def genEmoji(base=None,mouth=None,eyes=None):
	matchstr = r'\\[uU]'
	def f(x):
		return "{}.svg".format('none' if x is None else re.sub(r'\\[uU]0*', '-', x.encode('unicode-escape').decode('utf-8'))[1:]) # get file name
	base = readSVG(f'twemoji/base/{f(base)}')
	mouth = readSVG(f'twemoji/mouth/{f(mouth)}')
	eyes = readSVG(f'twemoji/eyes/{f(eyes)}')
	base.paste(mouth, (0, 0), mouth)
	base.paste(eyes, (0, 0), eyes)
	return base


testStr = "🏃🏻‍♀️"
# print("\U0001f3c3\U0001f3fb\u200d\u2640\ufe0f")
genEmoji(testStr, "\U0001f9d1\U0001f3fb").show()

# 1f9d1-1f3fb-200d-1f527