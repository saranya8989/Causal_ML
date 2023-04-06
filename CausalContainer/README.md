# ContainerSingE
Singularity definition files and scripts used to builld the container used in <i>Selecting Robust Features for Machine Learning Applications using Multidata Causal Discovery</i>.

<b>common_files</b>: this folder includes utility files, such as common bash scripts (e.g., those used to perform common container operations, such as launching jupyter notebook). In order to build the container, <b>a miniconda installer package named "miniconda.sh" must be placed inside this folder</b>. You can download the latest <a href="https://docs.conda.io/en/latest/miniconda.html" target="_blank" rel="noopener noreferrer">from the Conda website</a>.

<b>conda_env_defs</b>: this folder includes files describing conda environment, generally generated using 'conda env export > <env_name>.yml'.

Note that the container was originally built on an computer running Ubuntu 22.04 Jammy and Singularity version 3.10.4-Jammy. You can build the container using the following command from a terminal on the CausalContainer directory: 
<i>sudo singularity build --nv container_files/RFMLA_Causal.sif definition_files/tigr_gpu.def </i>

Remember to add the appropriate tags (e.g., --nv, --rocm, --nvcli) when building the environment, as it requires this tag to access the CUDA libraries used to access the GPU! This also means that you need to ensure that the appropriate CUDA drivers have been installed on both the computer used to build the container as well as the host computer where the container will be run (e.g., a university cluster)

Note that mamba is used in silent mode when installing the packages onto the container in order to avoid excessive artefacts being printed to the console, so it might seem like the building of the container is stalled since the installation can take several minutes at this stage.

Container structure based on the ContainerSingE repository:
https://github.com/msgomez06/ContainerSingE/
