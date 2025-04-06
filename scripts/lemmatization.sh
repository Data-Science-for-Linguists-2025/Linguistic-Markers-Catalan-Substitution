#!/usr/bin/env bash

#SBATCH --job-name=proj_lemmatization
#SBATCH --output=lemmatization.out 
#SBATCH --nodes=1
#SBATCH --ntasks=3
#SBATCH --partition=smp
#SBATCH --cluster=smp
#SBATCH --mem-per-cpu=16000
#SBATCH --time=180

module load python/ondemand-jupyter-python3.11
python lemmatization_script.py
'''
