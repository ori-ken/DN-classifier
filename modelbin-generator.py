#!/usr/bin/python3

import platform
import datetime
import os
import sys
import subprocess 

_script_version = "1.0"
_version = ""

_home_path = ""

def log(sformat, *args):
	now = datetime.datetime.now()
	sformat = now.strftime("%Y-%m-%d %H:%M:%S") + " [" + _version + "] " + sformat
	print(sformat % (args))
	return


if __name__ == '__main__':
# pre section
	_version = platform.python_version() 
	log("script version : %s", _script_version)
	_home_path = os.path.dirname(__file__)
	log("home path      : %s", _home_path)

# main section

	sys.exit(0)

