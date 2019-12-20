from itertools import tee

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

listofspecies = open('bacreduced.txt')

with open('Bac16s.faa', 'r') as fastaFile:
    for currentLine, nextLine in pairwise(fastaFile) :
        for x in listofspecies:
            names = x.split("_")
            if re.findall(names[0].strip(), currentLine):
                if re.findall(names[1].strip(), currentLine):
                    print ('>' + currentLine + nextLine)
