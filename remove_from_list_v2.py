import sys

filename = sys.argv[1]
listofspecies = []

listfile = open(sys.argv[2], 'r')
for line in listfile:
    x = line.rstrip()
    listofspecies.append(x)

with open(f"{filename}.filtered", "w") as outfile:
    with open(filename, "r") as infile:
        skip = False
        for line in infile:
            if any(species in line for species in listofspecies):
                skip = True
            elif skip:
                if line.startswith(">"):
                    skip = False
            else:
                outfile.write(line)
