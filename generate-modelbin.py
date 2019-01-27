#!/usr/bin/python3

import platform
import datetime
import sys
 
import MeCab
import fastText

_script_version = "1.0"
_version = ""

def log(sformat, *args):
	now = datetime.datetime.now()
	sformat = now.strftime("%Y-%m-%d %H:%M:%S") + " [" + _version + "] " + sformat
	print(sformat % (args))
	return

if __name__ == '__main__':

	_version = platform.python_version() 
	log("script version : %s", _script_version)

	mecab = MeCab.Tagger("-Owakati")
	log("positive data making ... ")
	f = open("/prod/git/scraping-rbp/scraping1.dat")
	fo = open("/prod/git/DN-classifier/model.txt", "w")
	line = f.readline()
	while line:
		wakati = mecab.parse(line)
		model_txt = "__label__1," + wakati
		fo.write(model_txt)
		line = f.readline()
	f.close
	fo.close

	log("negative data making ... ")
	f = open("/prod/git/scraping-rbp/scraping2.dat")
	fo = open("/prod/git/DN-classifier/model.txt", "a")
	line = f.readline()
	while line:
		wakati = mecab.parse(line)
		model_txt = "__label__2," + wakati
		fo.write(model_txt)
		line = f.readline()
	f.close
	fo.close
	log("output \"model.txt\"")

	log("model binary making ...")
	classifier = fastText.supervised("model.txt", "model.bin")
	log("output \"model.bin\"")

	sys.exit(0)

