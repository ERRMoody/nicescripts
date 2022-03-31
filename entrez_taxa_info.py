from Bio import Entrez
from Bio import SeqIO
import sys

accessions = []

with open (sys.argv[1], 'r') as filename:
	for line in filename:
		line = line.strip()	
		accessions.append(line)

print ("Accession,Species,Phylum,Kingdom,Domain")

for taxa in accessions:
	idvariable = taxa
	Entrez.email = 'Edmund.Moody@bristol.ac.uk'
	handle = Entrez.esearch(db="assembly", term=idvariable)
	record = Entrez.read(handle)
	idlist = (record['IdList'])
	idx = idlist[0]
	handle = Entrez.esummary(db="assembly", id=idx, retmode="text")
	record = Entrez.read(handle)
	for key, value in record.items():
		for x,y in value.items():
			boop = str(y[0])
			beep = boop.split(',')
			for fu in beep:
				if 'SpeciesTaxid' in fu:
					bar = fu.split(':')
					glomp = bar[1].strip(" '")
					taxid = glomp
				elif 'SpeciesName' in fu:
					bar = fu.split(':')
					glomp = bar[1].strip(" '")
					speciesname = glomp
	handle = Entrez.efetch(db="taxonomy", id=taxid, retmode ="xml")
	record = Entrez.read(handle)
	phylum1 = {d['Rank']:d['ScientificName'] for d in record[0]['LineageEx'] if d['Rank'] in ['phylum']}
	domain1 = {d['Rank']:d['ScientificName'] for d in record[0]['LineageEx'] if d['Rank'] in ['superkingdom']}
	kingdom1 = {d['Rank']:d['ScientificName'] for d in record[0]['LineageEx'] if d['Rank'] in ['kingdom']}

	phylum2 = str(phylum1)
	phylum3 = phylum2.split(':')

	kingdom2 = str(kingdom1)
	kingdom3 = kingdom2.split(':')

	domain2 = str(domain1)
	domain3 = domain2.split(':')
	
	kingdom = "N/A"
	domain = "N/A"
	phylum = "N/A"

	if len(phylum3) > 1:
		phylum = phylum3[1].strip("{} '")
	
	if len(kingdom3) > 1:
		kingdom = phylum3[1].strip("{} '")
	
	if len(domain3) > 1:
		domain = domain3[1].strip("{} '")
	

	print (taxa, speciesname, phylum, kingdom, domain, sep = ',')
