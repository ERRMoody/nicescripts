from ete3 import Tree
import sys
counter = 0
input_file = open(sys.argv[1], 'r')


for line in input_file:
	names = []
	t = Tree(line)
	for leaf in t:
		tipstring1 = leaf.name		
		tipstring = tipstring1.split("|")
		gene=tipstring[0]
		spec=tipstring[1]
		spec2 = spec.split("-")
		leaf.name = spec2[0] + "|" + gene
		names.append(leaf.name)
		counter = names.count(leaf.name)
		if counter > 1:
			leaf.name = leaf.name + '_' + str(counter)

	print (t.write(format=2))
