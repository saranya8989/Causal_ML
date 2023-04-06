#!/bin/bash



for tau_min in 8 
do
    for tau_max in 24
    do
        for pc_alpha in  .0000001 .00000015 .0001 .00015 .000015 .00001 .0000015 .000001 .001 .0015 .01 .015 .02 .03 .04 .05 .06 .07 .08 .09 .1 .15 .2 .25 .3 .35 .4 .45 .5 .55 .6 .65 .7 .75 .8 .85 .86 .88 .9 
        do
		for alpha_level in .1 
		do
			for seed in 12348 #50 12351 12352 12353 12354 12355 12356 12357 12359
			do
				sbatch --mail-type ALL --mail-user ssudhees@unil.ch --chdir /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/ --job-name tigramite_test --output /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/logs/con-%j.out --error /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/logs/err-%j.err --partition cpu --nodes 1 --ntasks 1 --cpus-per-task 1 --mem 64G --time 32:00:00 --wrap "module purge; module load gcc; source ~/.bashrc ; conda activate /work/FAC/FGSE/IDYST/tbeucler/default/saranya/miniconda3/envs/unil_tigramite ;python /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/run_pcstable_allwp_aligned.py $tau_min $tau_max $pc_alpha $alpha_level $seed"
			done
		done
	done
    done
done
