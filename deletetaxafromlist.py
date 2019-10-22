import sys
import subprocess

filename = sys.argv[1]
listofspecies = []
bacfile = open('./bacterialist', 'r')
for line in bacfile:
    x = line.rstrip()
    listofspecies.append(x)

for i in listofspecies:
    subprocess.call(['sed -i -e "s/>'+i+'/,+1d/g" '+filename+''],shell=True)

