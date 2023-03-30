import csv

with open('LCA_map.tsv', 'r') as tsv_file:
    reader = csv.reader(tsv_file, delimiter='\t')
    output_rows = []
    for row in reader:
        # Check if the length of the 2nd column is 2
        if len(row[1]) == 2:
            # Split the 2nd column into two separate rows
            output_rows.append([row[0], row[1][0]])
            output_rows.append([row[0], row[1][1]])
        else:
            # Keep the original row
            output_rows.append(row)

# Write the output to a new TSV file
with open('LCA_map_modified.tsv', 'w') as tsv_file:
    writer = csv.writer(tsv_file, delimiter='\t')
    writer.writerows(output_rows)

    
    #this script turns a map with multiple COG categories for a given KEGG_KO into multiple rows, for ease later...
