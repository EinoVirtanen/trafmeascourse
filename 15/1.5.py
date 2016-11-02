import os
import subprocess
tracedir = '/work/courses/unix/T/ELEC/E7130/general/trace/'
continues = os.popen('ls ' + tracedir + 'flow-continue/')
continuesfilelist = continues.read().split("\n")
continuesfiledwithzeros = open('continueslengthswithzeros', 'w')
counter = 0 # remove
for continuesfile in continuesfilelist:
	rows = os.popen('gunzip -c ' + tracedir + 'flow-continue/' + continuesfile)
	for row in rows:
		tmprow = row.split('\t')
		try:
			if counter % 1000 == 0:
				continuesfiledwithzeros.write(str(float(tmprow[10])-float(tmprow[9])) + ',')
			counter = counter + 1
		except:
			pass
continuesfiledwithzeros.close()
