#!/bin/bash
#SBATCH --job-name=Kegg2_LBCA
#SBATCH --output=kegg2_LBCA_%A_%a.out
#SBATCH --partition=med
#SBATCH --time=7-12:00:00
#SBATCH --array=1-7560
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=100GB
#SBATCH --nodes=1
## --cpu_bind=v,threads

JOB_ARRAY_FILE=`find ./ -iname "*.ale" | sort -V  | sed -n "${SLURM_ARRAY_TASK_ID}p"`

ID=`basename -s .ale "${JOB_ARRAY_FILE}"`
ALIGNMENT="${ID}.ale"

# extract the partial ID from the filename
PARTIAL_ID=$(basename "${ALIGNMENT}" | cut -d '.' -f 1)

# find the corresponding line in the table and extract the 2nd column value
TABLE_FILE="K2_OR_MAP.tsv"
newvariable=$(grep "$PARTIAL_ID" "$TABLE_FILE" | awk '{print $2}')

# run the SLURM job command with the newvariable added
srun ALEml_undated LBCA_sp_rooted.tre "${ALIGNMENT}" separators=- fraction_missing=fraction_missing.csv rate_multiplier:O:1397:"${newvariable}"
