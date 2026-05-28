from Bio import SeqIO
import sys

inputf = sys.argv[1]
outputf = sys.argv[2]

# A dictionary to store the longest record found for each ID
longest_sequences = {}

for record in SeqIO.parse(inputf, 'fasta'):
    # If we have seen this ID before, compare lengths
    if record.id in longest_sequences:
        if len(record.seq) > len(longest_sequences[record.id].seq):
            # If the new one is longer, it becomes the new reigning champion
            longest_sequences[record.id] = record
    else:
        # If it is the first time seeing this ID, add it to the dictionary
        longest_sequences[record.id] = record

# Write the final dictionary of longest sequences to the output file
# Using 'w' to ensure we never fall into the append-mode trap again!
with open(outputf, 'w') as outFile:
    SeqIO.write(list(longest_sequences.values()), outFile, 'fasta')
