#!/bin/bash

(
    cd $(dirname $0) 
    docker run -p 8888:8888 --rm -it --name=jupyter \
        -u ${UID}:$(id -g) \
        -v ~/:/home/jovyan \
        -v ${PWD}/support:/opt/conda/lib/python3.6/site-packages/support \
        -e JUPYTER_ENABLE_LAB=1 \
        jupyter-scipy-notebook-opencv:latest \
        start-notebook.sh \
        --NotebookApp.token='' \
        --NotebookApp.iopub_data_rate_limit=100000000
)

