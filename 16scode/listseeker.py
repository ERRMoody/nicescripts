#import re
#
#listofspecies = open("bacreduced.txt").readlines()
#


listofspecies = open("bacreduced.txt").readlines()
species_1 = []
species_2 = []
for line in listofspecies:
    species = line.strip().split('_')
    species_1.append(species[0])
    species_2.append(species[1])

species_1 = frozenset(species_1)
species_2 = frozenset(species_2)

with open("Bac16s.faa") as f:
    for line in f:
        if not line[0] == '>':
            continue
        line_tokens = line[1:].strip().split('_')
        if (line_tokens[0] in species_1) and (line_tokens[1] in species_2):
            print(line_tokens[0] + '_' + line_tokens[1])
# from collections import Counter
# wordcount = Counter('Bac16s.faa'.read().split())
#
# #listofseqs = open("Bac16s.faa").readlines()
#
# #for x in listofspecies:
# #    for i in range(0,len(listofseqs)):
# #        #print (i)
# #        names = x.split("_")
# #        if re.findall(names[0].strip(), listofseqs[i]):
# #            if re.findall(names[1].strip(), listofseqs[i]):
# #                print (">" + x + listofseqs[i+1].strip())
# #                break
#
#
#
#
# with open("Bac16s.faa", "r") as listofseqs:
#     wordcount = Counter('Bac16s.faa'.read().split())
#     for x in listofspecies:
#         for i in range(0,len(wordcount)):
#             print (i)
#             names = x.split("_")
#             if re.findall(names[0].strip(), listofseqs[i]):
#                 if re.findall(names[1].strip(), listofseqs[i]):
#                     print (">" + x + listofseqs[i+1].strip())
#                     break
# #
#
#
# listofspecies = open("bacreduced.txt").readlines()
# species_1 = []
# species_2 = []
# for line in listofspecies:
#     species = line.strip().split('_')
#     species_1.append(species[0])
#     species_2.append(species[1])
#
# species_1 = frozenset(species_1)
# species_2 = frozenset(species_2)
#
# with open("Bac16s.faa") as f:
#     for line in f:
#         if not line[0] == '>':
#             continue
#         line_tokens = line[1:].strip().split('_')
#         if (line_tokens[0] in species_1) and (line_tokens[1] in species_2):
#             print(line_tokens[0] + '_' + line_tokens[1])

# listofspecies = open("bacreduced.txt").readlines()
# species_list = []
# for line in listofspecies:
#     species = line.strip()
#     species_list.append(species)
#
# species_set = frozenset(species_list)
#
# with open("Bac16s.faa") as f:
#     for line in f:
#         if not line[0] == '>':
#             continue
#         stripped_line = line[1:].strip()
#         if stripped_line in species_set:
#             print(stripped_line)
