import os
import subprocess

continuesports = {}
expiresports = {}

tracedir = '/work/courses/unix/T/ELEC/E7130/general/trace/'

continues = os.popen('ls ' + tracedir + 'flow-continue/')
expires = os.popen('ls ' + tracedir + 'flow-expire/')

continuesfilelist = continues.read().split("\n")
expiresfilelist = expires.read().split("\n")

for continuesfile in continuesfilelist:
	rows = os.popen('gunzip -c ' + tracedir + 'flow-continue/' + continuesfile)
	for row in rows:
		tmprow = row.split('\t')
		if(len(tmprow) > 9):
			if tmprow[5] in continuesports:
				continuesports[tmprow[5]] = continuesports[tmprow[5]] + 1
			else:
				continuesports[tmprow[5]] = 1

for expiresfile in expiresfilelist:
	rows = os.popen('gunzip -c ' + tracedir + 'flow-expire/' + expiresfile)
	for row in rows:
		tmprow = row.split('\t')
		if(len(tmprow) > 9):
			if tmprow[5] in expiresports:
				expiresports[tmprow[5]] = expiresports[tmprow[5]] + 1
			else:
				expiresports[tmprow[5]] = 1


continuesfile = open('continuesports', 'w')

for continuesport in continuesports:
	continuesfile.write(continuesport + ',' + str(continuesports[continuesport]) + '\n')

continuesfile.close()

expiresfile = open('expiresports', 'w')

for expiresport in expiresports:
	expiresfile.write(expiresport + ',' + str(expiresports[expiresport]) + '\n')

expiresfile.close()
