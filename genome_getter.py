import sys
from Bio import SeqIO

archaea_list = []
sequences = []


with open("archaeagenomes.csv") as file:
    while line := file.readline():
        archaea_list.append((line.rstrip()))



for archaea in archaea_list:
	for record in SeqIO.parse(sys.argv[1], "fasta"):
		if archaea in record.id:
			sequences.append(record)



with open ("archaealsubsample.faa", "w") as output_handle:
	SeqIO.write(sequences, output_handle, "fasta")


