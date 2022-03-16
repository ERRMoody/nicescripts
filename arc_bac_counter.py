import sys
from Bio import SeqIO

archaea_counter = 0
bacteria_counter = 0
number_of_taxa = 0

with open('arc.csv', 'r') as f:
    arc_taxa_list = [line.strip() for line in f]


with open('bac.csv', 'r') as f:
    bac_taxa_list = [line.strip() for line in f]

for record in SeqIO.parse(sys.argv[1], "fasta"):
	for taxa in arc_taxa_list:
		if taxa in str(record.id):
			archaea_counter += 1
	for taxa in bac_taxa_list:
		if taxa in str(record.id):
			bacteria_counter += 1

print (str(sys.argv[1]), archaea_counter, bacteria_counter, sep=',')
