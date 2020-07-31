from Bio import AlignIO
import sys

input_handle = open(sys.argv[1], "rU")
output_handle = open(sys.argv[2], "w")

alignments = AlignIO.read(input_handle, "fasta")
counter = 0

for record in alignments:
    counter = counter + 1
    record.id = str(counter) + record.id

AlignIO.write(alignments, output_handle, "phylip")

output_handle.close()
input_handle.close()

