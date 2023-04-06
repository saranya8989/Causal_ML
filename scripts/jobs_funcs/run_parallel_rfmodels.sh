#!/bin/bash

for pc_alpha in 0.001 0.00015 0.0001 0.0015 0.01 0.015 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.86 0.88 0.9 
do
	sbatch --mail-type ALL --mail-user ssudhees@unil.ch --chdir /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/ --job-name tigramite_test --output /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/logs/con-%j.out --error /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/logs/err-%j.err --partition cpu --nodes 1 --ntasks 1 --cpus-per-task 1 --mem 64G --time 32:00:00 --wrap "module purge; module load gcc; source ~/.bashrc ; conda activate /work/FAC/FGSE/IDYST/tbeucler/default/saranya/miniconda3/envs/unil_tigramite ;python /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/train_rf_models.py $pc_alpha"
done
