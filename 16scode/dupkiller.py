from Bio import SeqIO

with open('bacreduced3.faa', 'a') as outFile:
    record_ids = list()
    for record in SeqIO.parse('bacreduced2.faa', 'fasta'):
        if record.id not in record_ids:
            record_ids.append( record.id)
            SeqIO.write(record, outFile, 'fasta')
