import pandas as pd
import sys

df1 = pd.read_csv(sys.argv[1], sep = '\t')
df2 = pd.read_csv(sys.argv[2])

df3 = pd.merge(df1,df2, on = 'Category')

# group by KEGG_ko and calculate the mean of the OR column
grouped_df = df3.groupby(['KEGG_ko'])['OR'].mean().rename('mean_OR')

# reset the index of the resulting dataframe and assign to grouped_df
grouped_df = grouped_df.reset_index()

# print the output DataFrame

grouped_df.to_csv(sys.argv[3], header=True, index=False, sep='\t')
