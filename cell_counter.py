import sys
from collections import defaultdict
import pandas as pd

df1 = pd.read_csv(sys.argv[1], sep='\t')

#df2 = df1.groupby(df1.columns.tolist(),as_index=False).size()

#print (df1)

dict = {k: g["COG_category"].tolist() for k,g in df1.groupby("KEGG_ko")}


#print (dict)


print ("KO", "highest_COG_cat", "difference_1st_and_2nd", "categories", "sequences", "top_COG_per_seq", "COG_cat", sep='\t')



for key, value in dict.items():
	counter={}
	seq_count = 0
	for x in value:
		counter[x] = value.count(x)
		seq_count = seq_count + 1
	sorted_counter = (sorted(counter.items(), key=lambda x: x[1], reverse=True))
	variable = sorted_counter[0]
	if len(sorted_counter) > 1 :
		variable2 = sorted_counter[1]	
		num1 = variable[1]
		num2 = variable2[1]

		difference = num1 - num2
	
		print (key, num1, difference, len(sorted_counter), seq_count, num1/seq_count, variable[0], sep='\t')
	else:
		print (key, variable[1], 0, len(sorted_counter), seq_count, variable[1]/seq_count, variable[0], sep='\t')
