from Bio import AlignIO
import sys

f = sys.argv[1]

alignment = AlignIO.read(open(f), "fasta")
amino_acids_total = alignment.get_alignment_length()


for record in alignment:
	gaps = 0
	for char in record.seq:
		if char == '-':
			gaps += 1
	proportions = gaps / amino_acids_total
	print (f, record.id, gaps, amino_acids_total, proportions)

