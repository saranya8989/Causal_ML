#!/bin/bash

source /opt/miniconda/etc/profile.d/conda.sh
conda activate PySing

cd ~

default_dir=/work/

# Check if configuration exists
if test -e ".jupyter/jupyter_notebook_config.json"; then
    read -p 'Please input the port number to use: ' port_num
        
    read -p "Do you want to change the running directory? (Default is $default_dir)? [y,n]: " doit 
   
    case $doit in  
      y|Y) read -p "Please input the path: " directory
            if ! [[ -d $directory ]]
            then
                echo "Directory doesn't exist, using $default_dir... "
                directory=$default_dir
                fi
            ;; 
      n|N) directory=$default_dir;; 
      *) echo "error, defaulting to $default_dir...."
         directory=$default_dir
         ;; 
    esac
    
    
    jupyter-notebook --ip=$(hostname -i) --port=$port_num --no-browser --port-retries=0 --notebook-dir=$directory &
    
    
else
    echo "configuration file doesn't exist!"
    echo 'Please run the notebook-setup app'
fi
