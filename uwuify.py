# -*- coding: utf-8 -*-
import re
import random
import pandas
import os

global faces
faces = ["(・`ω´・)", "owo", "UwU", ">w<", "^w^"]


#Credit to https://honk.moe/tools/owo.html
#for the regex (in case i share this idk)
def regex_hell(text):
	if ("<color=" in text):
		match = re.findall("<color=([^<]*)>", text)
		for x in match:
			text = text.replace(x, "#ff89f1")
		return text

	if ((text == "nan") or (text == "NaN") or (text == "")):
		return ""
	if (("http" in text) or ("<" in text) or ("{" in text) or ("gaijin.net" in text) or ((" " not in text) and (len(text) > 15)) or (text == "title")):
		#print("skipped")
		return text

	text = re.sub("(?:r|l)", "w", text)
	text = re.sub("(?:R|L)", "W", text)
	text = re.sub("/n([aeiou])", 'ny$1', text)
	text = re.sub("/N([aeiou])", 'Ny$1', text)
	text = re.sub("/N([AEIOU])", 'Ny$1', text)
	text = re.sub("/ove/g", "uv", text)
	text = re.sub("[!]", " " + faces[random.randint(0,4)], text)
	return text


Path = "C:\Program Files (x86)\Steam\steamapps\common\War Thunder\lang\\"
filelist = os.listdir(Path)

for i in filelist:
	if i.endswith(".csv"):
		csvFile = pandas.read_csv(Path + i, sep=';')
		csvFile["<English>"] = csvFile["<English>"].apply(lambda x: regex_hell(str(x)))
		csvFile.to_csv(Path + i, encoding='utf-8', sep=";", index=False)
		#print(csvFile)
input("Finished")


#call "D:\Code\Python Versions\3.7.3\python.exe" "uwuify.py"