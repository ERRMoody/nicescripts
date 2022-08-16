from ete3 import Tree
import sys


t = Tree(sys.argv[1])

with open(sys.argv[2]) as f:
    prune_list = [line.rstrip() for line in f]

pruney_list = []

for node in t:
	for i in prune_list:
		if i in str(node):
			pruney_list.append(node)
#			node.delete()
t.prune(pruney_list)

t.write(format=9, outfile=sys.argv[3])

