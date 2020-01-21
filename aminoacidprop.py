from Bio import SeqIO
import glob
import sys
import pandas as pd

def count_occurence(f, amino_acids_to_track='ACDEFGHIKLMNPQRSTVWY'):
    amino_acids_per_train = 0
    amino_acids = dict.fromkeys(amino_acids_to_track, 0)
    # or amino_acids = { k: 0 for k in amino_acids_to_track}

    for record in SeqIO.parse(f, "fasta"):
        for char in record.seq:
            if char in amino_acids:
                amino_acids_per_train += 1
                amino_acids[char] += 1

    proportions  = { k : (v) / amino_acids_per_train for k, v in amino_acids.items()}
    return proportions

def write_output(out_filename, from_file, proportions):
    with open(out_filename, 'a+') as out_file:
        out_file.write('amino acid,proportion,species\n')
        for k, v in proportions.items():
            out_file.write('{},{},{}\n'.format(k, v, from_file))

if __name__ == '__main__':
    out_file = (sys.argv[2])
    f = sys.argv[1]
    proportions = count_occurence(f)
    write_output(out_file, f, proportions)
    df = pd.read_csv(out_file) 
    df = df.pivot_table('proportion', ['species'], 'amino acid')
    df = df.groupby(['species'])['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'].mean()
    df.to_csv(out_file)
