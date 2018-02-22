FROM jupyter/scipy-notebook
RUN cd /opt/conda && conda install --yes opencv

