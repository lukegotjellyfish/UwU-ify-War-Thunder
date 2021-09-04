# -*- coding: utf-8 -*-
import re
import random
import pandas
import os
from tkinter import filedialog
from tkinter import *

global faces
faces = ["(・`ω´・)", "owo", "UwU", ">w<", "^w^"]

def regexHell(text):
	text = re.sub("(?:r|l)", "w", text)
	text = re.sub("(?:R|L)", "W", text)
	text = re.sub("/n([aeiou])", 'ny$1', text)
	text = re.sub("/N([aeiou])", 'Ny$1', text)
	text = re.sub("/N([AEIOU])", 'Ny$1', text)
	text = re.sub("/ove/g", "uv", text)
	text = re.sub("[!]", " " + faces[random.randint(0,4)], text)
	return text

#Credit to https://honk.moe/tools/owo.html for the regex
def processText(text):
	if ("<color=" in text):
		match = re.findall("<color=([^<]*)>", text)
		for x in match:
			text = text.replace(x, "#ff89f1")
		return text

	if ((text == "nan") or (text == "NaN") or (text == "")):
		return ""
	if (("http" in text) or ("<" in text) or ("gaijin.net" in text) or ((" " not in text) and (len(text) > 15)) or (text == "title")):
		#print("skipped")
		return text

	splitText = text.split(" ")
	text = ""
	for word in splitText:
		if "{" in word:
			text += word
			#input("text: ["+text+"] { in word: " + word)
		else:
			#print("word: " + word)
			text += regexHell(word)
			#print("new word: " + word)
		if word != splitText[-1]:
			text += " "

	#text = regexHell(text)
	return text

root = Tk()
root.withdraw()
Path = filedialog.askdirectory(initialdir = "/",title = "Select War Thunder Lang Folder")
#Path = "C:/Program Files (x86)/Steam/steamapps/common/War Thunder/lang/"
filelist = os.listdir(Path)

for i in filelist:
	if i.endswith(".csv"):
		csvFile = pandas.read_csv(Path + "/" + i, sep=';')
		csvFile["<English>"] = csvFile["<English>"].apply(lambda x: processText(str(x)))
		csvFile.to_csv(Path + i, encoding='utf-8', sep=";", index=False)
		print("File: [" + i + "]")
		print(csvFile)
input("Finished")