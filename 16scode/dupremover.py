#Didn't test this but probably works.
fasta_file = open("bacreduced.faa")
fasta_read = fasta_file.readlines() #assuming can be read into memory, otherwise read in a while loop.
fasta_file.close()

seq_dict = {}
cur_id = ""; cur_seq = ""
for line in fasta_read:
    if line[0] == ">":
        if cur_id != "":
            seq_dict[cur_id] = cur_seq
        cur_id = line[1:].strip()
        cur_seq = ""
    else:
        cur_seq += line.strip()
seq_dict[cur_id] = cur_seq
#seq_dict should have dereplicated reads because if key is repeated, will overwrite original value of key in dict.
#to write to new file...
out_file = open("bacreduced2.faa", "w")
for seq_key in seq_dict:
    out_file.write(">%s\n%s\n" %(seq_key, seq_dict[seq_key]))
out_file.close()
