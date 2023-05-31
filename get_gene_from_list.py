import sys
from Bio import SeqIO

thing_list = []
sequences = []

with open(sys.argv[2]) as file:
    for line in file:
        line = line.strip()
        if line:
            thing_list.append(line)

new_file = str(sys.argv[1]) + '_modified'

for thing in thing_list:
    for record in SeqIO.parse(sys.argv[1], "fasta"):
        if thing in record.id:
            sequences.append(record)

with open(new_file, "w") as output_handle:
    SeqIO.write(sequences, output_handle, "fasta")
