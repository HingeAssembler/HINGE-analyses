# HINGE-analyses
Analysis accompanying  "HINGE: Long-Read Assembly Achieves Optimal Repeat Resolution" http://biorxiv.org/content/early/2016/07/05/062117

The following software needs to be installed

```
build-essential
libhdf5-dev
libboost-all-dev
cmake-3.2
g++-4.9
gcc-4.9
python
python-pip
```

We also need [Aspera connect](

###Instructions to install

```
git clone https://github.com/govinda-kamath/HINGE-analyses.git
cd HINGE-analyses
git submodule foreach --recursive git submodule update --init
git submodule update --init --recursive
./build.sh
source setup.sh
# Optionally you can create a python virtual environment and then install the requirements
pip install -r requirements.txt 
```


The results of Figure 2 paper can be reproduced in [this](https://github.com/govinda-kamath/HINGE-analyses/blob/master/HINGE_pipeline_NCTC.ipynb) notebook.


