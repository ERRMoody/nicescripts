import sys

from Bio import SeqIO

import pandas as pd


df1 = pd.read_csv(sys.argv[1], skiprows=4, sep='\t')

ko_frame = df1[["KEGG_ko","Description","Preferred_name","eggNOG_OGs"]]

ko_frame['COG'] = ko_frame['eggNOG_OGs'].str.split('@').str[0]

ko_frame = ko_frame.drop("eggNOG_OGs", axis = 1)

ko_frame = ko_frame[~ko_frame.KEGG_ko.str.contains("-", na=False)]

ko_frame = ko_frame[~ko_frame.KEGG_ko.str.contains(",", na=False)]

ko_frame = ko_frame.dropna(subset=['KEGG_ko'])

ko_frame = ko_frame.drop_duplicates()


ko_frame.to_csv('Annotations_duplicates_dropped.csv', index=False)
