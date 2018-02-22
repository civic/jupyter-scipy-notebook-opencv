#!/bin/bash

(
    cd $(dirname $(realpath $0)) 
    docker run -p 8888:8888 --rm -it --name=jupyter \
        -u ${UID}:$(id -g) \
        -v ~/:/home/jovyan \
        -v ${PWD}/support:/opt/conda/lib/python3.6/site-packages/support \
        jupyter-scipy-notebook-opencv:latest \
        start-notebook.sh \
        --NotebookApp.token='' \
        --NotebookApp.iopub_data_rate_limit=100000000
)

