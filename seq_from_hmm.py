from Bio import SeqIO
from Bio import SearchIO
import sys

hit_ids = []
sequences = []


with open (sys.argv[1], 'r') as input:
	for result in SearchIO.parse(input, 'hmmsearch3-domtab'):
		hits = result.hits
		num_hits = len(hits)	
		for x in range(num_hits):
			hit_ids.append(hits[x].id)


for record in SeqIO.parse(sys.argv[2], "fasta"):
	if record.id in hit_ids:
		sequences.append(record)


output = str(sys.argv[1]) + '.hmmered_fasta'

SeqIO.write(sequences, output, "fasta")

