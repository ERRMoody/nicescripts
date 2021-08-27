for sample in *newick; do gawk -v RS='[-+]?[0-9.]+[eE][-+][0-9]+'  -v CONVFMT=%.10f '{print $0 (RT == ""?"" :+RT)}' ${sample} | tr -d '\n' > ${sample}_v2; done
