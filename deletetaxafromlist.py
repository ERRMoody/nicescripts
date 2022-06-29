import sys
import subprocess

filename = sys.argv[1]
listofspecies = []

listfile = open(sys.argv[2], 'r')
for line in listfile:
    x = line.rstrip()
    listofspecies.append(x)

for i in listofspecies:
    subprocess.call(['sed -i -e "/>'+i+'/,+1d" '+filename+''],shell=True)

