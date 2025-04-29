#!/usr/bin/env bash

#SBATCH --job-name=radioteca_scrape
#SBATCH --output=radioteca_scrape.out
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=smp
#SBATCH --cluster=smp
#SBATCH --mem-per-cpu=16000
#SBATCH --time=960
#SBATCH --cpus-per-task=8
#SBATCH --ntasks-per-node=1

module load python/ondemand-jupyter-python3.11
python radioteca_scrape.py

