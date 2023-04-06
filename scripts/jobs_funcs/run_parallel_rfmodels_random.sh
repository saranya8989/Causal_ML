#!/bin/bash

for n in $(seq 10 10 1000) 
do
	sbatch --mail-type ALL --mail-user ssudhees@unil.ch --chdir /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/ --job-name tigramite_test --output /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/logs/con-%j.out --error /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/logs/err-%j.err --partition cpu --nodes 1 --ntasks 1 --cpus-per-task 1 --mem 64G --time 32:00:00 --wrap "module purge; module load gcc; source ~/.bashrc ; conda activate /work/FAC/FGSE/IDYST/tbeucler/default/saranya/miniconda3/envs/unil_tigramite ;python /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/train_rf_models_random.py $n"
done
