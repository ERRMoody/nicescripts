import sys

filename = sys.argv[1]
listofspecies = []

with open(sys.argv[2], 'r') as listfile:
    for line in listfile:
        x = line.rstrip()
        listofspecies.append(x)

with open(f"{filename}.filtered", "w") as outfile:
    with open(filename, "r") as infile:
        skip = False
        for line in infile:
            if line.startswith(">"):
                # Check if any species is in the header line
                if any(species in line for species in listofspecies):
                    skip = True
                else:
                    skip = False
            if not skip:
                outfile.write(line)
