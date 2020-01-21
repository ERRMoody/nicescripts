import pandas as pd
import sys
import os 
import subprocess

df1 = pd.read_csv(sys.argv[1], sep='\t', quoting=3)

filename = str(sys.argv[1])
outputfile = filename.strip('.log')

dfLUCA = df1[['end_61']]
dfLBCA = df1[['end_60']]
dfLACA = df1[['end_42']]

lucafas = outputfile + 'luca.fa'
lbcafas = outputfile + 'lbca.fa'
lacafas = outputfile + 'laca.fa'

dfLUCA.to_csv(lucafas, index=False)
dfLBCA.to_csv(lbcafas, index=False) 
dfLACA.to_csv(lacafas, index=False)

subprocess.call(['sed -i -e "s/,//gi" '+lucafas+' '], shell=True)
subprocess.call(['sed -i -e "s/,//gi" '+lbcafas+' '], shell=True)
subprocess.call(['sed -i -e "s/,//gi" '+lacafas+' '], shell=True)


subprocess.call(['sed -i -e "s/end/>end/gi" '+lucafas+' '], shell=True)
subprocess.call(['sed -i -e "s/end/>end/gi" '+lbcafas+' '], shell=True)
subprocess.call(['sed -i -e "s/end/>end/gi" '+lacafas+' '], shell=True)

subprocess.call(['sed -i -e "s/\\"//gi" '+lucafas+' '], shell=True)
subprocess.call(['sed -i -e "s/\\"//gi" '+lbcafas+' '], shell=True)
subprocess.call(['sed -i -e "s/\\"//gi" '+lacafas+' '], shell=True)
