from Bio import SeqIO

import sys

gene = input("Enter partial string within fasta id:")

output = gene + '.fasta'
sequences = []

for record in SeqIO.parse(sys.argv[1], "fasta"):
	if gene in record.id:
		sequences.append(record)




with open(output, "w") as output_handle:
    SeqIO.write(sequences, output_handle, "fasta")
