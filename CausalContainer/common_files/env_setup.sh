#!/bin/bash
source /opt/miniconda/etc/profile.d/conda.sh
export PATH=/opt/miniconda/bin:$PATH
export PYTHONPATH=/opt/miniconda3/bin:$PATH
export CONDA_ALWAYS_YES="true"

conda update -n base conda -q
conda install -c conda-forge mamba -q
mamba env create -f /opt/environment.yml -q

conda clean --all --yes

export CONDA_ALWAYS_YES="false"
