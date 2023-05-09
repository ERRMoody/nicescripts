from Bio import SeqIO
import sys
import hashlib

inputf = sys.argv[1]
outputf = sys.argv[2]

hashes = set()

with open(outputf, 'a') as outFile:
    for record in SeqIO.parse(inputf, 'fasta'):
        seq_hash = hashlib.md5(str(record.seq).encode('utf-8')).hexdigest()
        if seq_hash not in hashes:
            hashes.add(seq_hash)
            SeqIO.write(record, outFile, 'fasta')
