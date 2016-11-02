import os
import subprocess
tracedir = '/work/courses/unix/T/ELEC/E7130/general/trace/'
continues = os.popen('ls ' + tracedir + 'flow-continue/')
continuesfilelist = continues.read().split("\n")
pairs = {}
for continuesfile in continuesfilelist:
	rows = os.popen('gunzip -c ' + tracedir + 'flow-continue/' + continuesfile)
	for row in rows:
		tmprow = row.split('\t')
		if len(tmprow) > 1 and len(tmprow[0].split(".")) > 3:
			pair = str(tmprow[0].split(".")[0]) + "," + str(tmprow[1].split(".")[0])
			if pair in pairs:
				pairs[pair] = pairs[pair] + 1
			else:
				pairs[pair] = 1
x = 0
for pair in pairs:
	x = x + 1
	print pair.split(",")[0] + ".0.0.0/8 -> " + pair.split(",")[1] + ".0.0.0/8," + str(pairs[pair])
