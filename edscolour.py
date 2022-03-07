from ete3 import Tree
import sys
import re

#This is Edmund R.R Mooody's script to convert a newick treefile into a coloured figtree file to aid with visualisation
#USAGE = python edscolour.py treefile.tre taxacolour.tsv > treefile.figtrecol

#establish dictionaries
colour_dict = {}
tip_list = []


#First argument is your treefile
t = Tree(sys.argv[1])


#Second argument is a tab-seperated file, in column one are partial names of tips present in your tree (i.e Cyano0001 would be Cyano) in column two, colour hexcodes (i.e #FF0000)
colourlist = open(sys.argv[2], "r")

for tip in t.traverse():
	tipname = str(tip.name)
	if re.search('[a-zA-Z0-9]', tipname):
		tip_list.append(tipname.strip())
	else:
		pass

for line in colourlist:
	x = line.split()
	y = "[&!color=" + str(x[1]) + "]"
	colour_dict[x[0]] = y


for idx, x in enumerate(tip_list):
	for key, value in colour_dict.items():
		if key in x:
			tip_list[idx] = str(x) + str(value)
			

print ("#NEXUS")
print ("begin taxa;")
print ("\tdimensions ntax=",len(tip_list),";")
print ("\ttaxlabels")
for x in tip_list:
	print("\t",x)
print (";")
print ("end;\n")
print ("begin trees;")
print ("\t tree tree_1 = [&R]", t.write())
print ("end;\n")
print ("begin figtree;")
print ('\tset appearance.backgroundColorAttribute="Default";')
print ('\tset appearance.backgroundColour=#ffffff;')
print ('\tset appearance.branchColorAttribute="User selection";')
print('\tset appearance.branchColorGradient=false;')
print('\tset appearance.branchLineWidth=1.0;')
print('\tset appearance.branchMinLineWidth=0.0;')
print('\tset appearance.branchWidthAttribute="Fixed";')
print('\tset appearance.foregroundColour=#000000;')
print('\tset appearance.hilightingGradient=false;')
print('\tset appearance.selectionColour=#2d3680;')
print('\tset branchLabels.colorAttribute="User selection";')
print('\tset branchLabels.displayAttribute="label";')
print('\tset branchLabels.fontName="Arial";')
print('\tset branchLabels.fontSize=10;')
print('\tset branchLabels.fontStyle=0;')
print('\tset branchLabels.isShown=true;')
print('\tset branchLabels.significantDigits=4;')
print('\tset layout.expansion=0;')
print('\tset layout.layoutType="RECTILINEAR";')
print('\tset layout.zoom=0;')
print('\tset legend.attribute="label";')
print('\tset legend.fontSize=10.0;')
print('\tset legend.isShown=false;')
print('\tset legend.significantDigits=4;')
print('\tset nodeBars.barWidth=4.0;')
print('\tset nodeBars.displayAttribute=null;')
print('\tset nodeBars.isShown=false;')
print('\tset nodeLabels.colorAttribute="User selection";')
print('\tset nodeLabels.displayAttribute="label";')
print('\tset nodeLabels.fontName="Arial";')
print('\tset nodeLabels.fontSize=10;')
print('\tset nodeLabels.fontStyle=0;')
print('\tset nodeLabels.isShown=false;')
print('\tset nodeLabels.significantDigits=4;')
print('\tset nodeShape.colourAttribute="User selection";')
print('\tset nodeShape.isShown=false;')
print('\tset nodeShape.minSize=10.0;')
print('\tset nodeShape.scaleType=Width;')
print('\tset nodeShape.shapeType=Circle;')
print('\tset nodeShape.size=4.0;')
print('\tset nodeShape.sizeAttribute="Fixed";')
print('\tset polarLayout.alignTipLabels=false;')
print('\tset polarLayout.angularRange=0;')
print('\tset polarLayout.rootAngle=0;')
print('\tset polarLayout.rootLength=100;')
print('\tset polarLayout.showRoot=true;')
print('\tset radialLayout.spread=0.0;')
print('\tset rectilinearLayout.alignTipLabels=false;')
print('\tset rectilinearLayout.curvature=0;')
print('\tset rectilinearLayout.rootLength=100;')
print('\tset scale.offsetAge=0.0;')
print('\tset scale.rootAge=1.0;')
print('\tset scale.scaleFactor=1.0;')
print('\tset scale.scaleRoot=false;')
print('\tset scaleAxis.automaticScale=true;')
print('\tset scaleAxis.fontSize=8.0;')
print('\tset scaleAxis.isShown=false;')
print('\tset scaleAxis.lineWidth=1.0;')
print('\tset scaleAxis.majorTicks=1.0;')
print('\tset scaleAxis.origin=0.0;')
print('\tset scaleAxis.reverseAxis=false;')
print('\tset scaleAxis.showGrid=true;')
print('\tset scaleBar.automaticScale=true;')
print('\tset scaleBar.fontSize=10.0;')
print('\tset scaleBar.isShown=true;')
print('\tset scaleBar.lineWidth=1.0;')
print('\tset scaleBar.scaleRange=0.0;')
print('\tset tipLabels.colorAttribute="User selection";')
print('\tset tipLabels.displayAttribute="Names";')
print('\tset tipLabels.fontName="Arial";')
print('\tset tipLabels.fontSize=12;')
print('\tset tipLabels.fontStyle=0;')
print('\tset tipLabels.isShown=true;')
print('\tset tipLabels.significantDigits=4;')
print('\tset trees.order=true;')
print('\tset trees.orderType="decreasing";')
print('\tset trees.rooting=false;')
print('\tset trees.rootingType="User Selection";')
print('\tset trees.transform=false;')
print('\tset trees.transformType="cladogram";')
print("end;")


