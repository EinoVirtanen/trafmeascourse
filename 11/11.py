import os
import subprocess
tracedir = '/work/courses/unix/T/ELEC/E7130/general/trace/'
continues = os.popen('ls ' + tracedir + 'flow-continue/')
continuesfilelist = continues.read().split("\n")

firstflow = 1392500000
lastflow  = 1393200000
timediff = lastflow-firstflow
increment = timediff/1000

flowsbytime = []
for i in range(1000):
	flowsbytime.append(0)

#continuesfiledwithzeros = open('continueslengthswithzeros', 'w')
counter = 0 # remove
for continuesfile in continuesfilelist:
	#rows = os.popen('gunzip -c ' + tracedir + 'flow-continue/' + continuesfile)
	rows = os.popen('cat short')
	i = 0
	for row in rows:
		i = i + 1
		if i > 35:
			tmprow = row.split('\t')
			if len(tmprow) > 9:
				avgtime = int((float(tmprow[9]) + float(tmprow[10]))/2)
				#data = int(tmprow[5])
				for i in range(1000):
					if ((firstflow + increment * i) >= avgtime) and ((firstflow + increment * (i + 1)) < avgtime):
						flowsbytime[i] = flowsbytime[i] + 1
print flowsbytime
#continuesfiledwithzeros.close()
