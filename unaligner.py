from Bio import SeqIO
from Bio.Seq import Seq
import sys

inputf = sys.argv[1]
outputf = sys.argv[2]

# Using 'w' mode to create a fresh file every time
with open(outputf, 'w') as outFile:
    for record in SeqIO.parse(inputf, 'fasta'):
        
        # Convert the sequence to a string and strip out any gap characters
        unaligned_seq = str(record.seq).replace('-', '').replace('.', '')
        
        # Turn it back into a Biopython Seq object
        record.seq = Seq(unaligned_seq)
        
        # Write the unaligned record to your new file
        SeqIO.write(record, outFile, 'fasta')
