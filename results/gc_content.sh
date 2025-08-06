#!/bin/bash -l

#$ -P bioinfo-ms
#$ -pe omp 4
#$ -pe omp 4

module load miniconda
source conda activate biopython_test

python gc_content_argparse.py -i GCF_014836715.1_ASM1483671v1_genomic.fna -o gc_result.txt
