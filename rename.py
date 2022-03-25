from ete3 import Tree
import sys
import pandas as pd


Taxonomy = pd.read_csv(sys.argv[2], sep='\t')

tax_dict = dict(zip(Taxonomy.BinID, Taxonomy.Taxonomy))

t = Tree(sys.argv[1])

output = str(sys.argv[1]) + '.renamed'

for key, value in tax_dict.items():
	for leaf in t:
		if key in leaf.name:
			leaf.name = leaf.name + value


t.write(format=2, outfile=output)

