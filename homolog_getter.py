#usage = sysarg1 for homologues, sysarg2 for annotated protein fasta

import sys
from Bio import SeqIO
import pandas as pd
#import pandas for dataframe management, and SeqIO from biopython for fasta manipulation

KO_dict = {}


#for record in SeqIO.parse(sys.argv[2], "fasta"):
#	protein_names.append(record.id)
#establish protein names from the fasta as a list

df1 = pd.read_csv(sys.argv[1], skiprows=4, sep='\t')
#establish the annotations output csv as a pandas dataframe, skipping the unnecesary information in the first 4 lines


kos = df1[["KEGG_ko","#query"]]

kos = kos[kos['KEGG_ko'].notna()]

kos_lists = kos.KEGG_ko.str.split(',')

kos.KEGG_ko = kos_lists                        

df2 = kos.explode('KEGG_ko')



KO_dict = df2.groupby('KEGG_ko')['#query'].apply(list).to_dict()

for KO, query in KO_dict.items():
	if 'K' in KO:
		x = KO.split(':')
		filename = x[1] + ".fasta"
		query_list = []
		for x in SeqIO.parse(sys.argv[2], "fasta"):
			for i in range(len(query)):
				if query[i] in x.id:
					query_list.append(x)

		
		SeqIO.write(query_list, filename, "fasta")




