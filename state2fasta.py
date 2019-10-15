import pandas as pd 
import sys

file = sys.argv[1]

df1 = pd.read_csv(file, sep='\t')

df2 = df1['State']


def main():
    print (">_" + sys.argv[1] + "ancestral_state_reconstruction")
    sequence = df2.to_string(index=False)
    fasta = []
    for i in sequence:
        i = i.strip()
        fasta.append(i)
    print (*fasta, sep='')
   
if __name__ == '__main__':
    main()
