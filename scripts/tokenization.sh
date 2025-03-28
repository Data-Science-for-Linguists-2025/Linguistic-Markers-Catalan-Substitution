#!/usr/bin/env bash

#SBATCH --job-name=proj_tokenization
#SBATCH --output=tokenization.out 
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --partition=smp
#SBATCH --cluster=smp
#SBATCH --mem-per-cpu=16000

module load python/ondemand-jupyter-python3.11
python tokenize_script.py
