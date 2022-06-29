from Bio import AlignIO
import sys

f1 = sys.argv[1]
f2 = sys.argv[2]


alignment = AlignIO.read(open(f1), "fasta")
trimmed = AlignIO.read(open(f2), "fasta")


list1 = []
list2 = []

for record in alignment:
	list1.append(record.id)
for record in trimmed:
	list2.append(record.id)

list3 = set(list1) - set(list2)

for i in list3:
	print (i, sep = ',')
