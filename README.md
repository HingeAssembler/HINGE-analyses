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

We also need [Aspera connect](http://downloads.asperasoft.com/en/downloads/8?list) to speed up the downloads.

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

We require the following python packages. All of can be installed with `sudo pip install <package>`, with exception of forceatlas2, which should be downloaded and installed from [here](https://pypi.python.org/pypi/ForceAtlas2/1.0) for better performance.

```
numpy
ujson
cython
forceatlas2
networkx
matplotlib
biopython
bcbio-gff
bcbio-nextgen
colormap
easydev
```


The results of Figure 2 in the paper can be reproduced using [this](https://github.com/govinda-kamath/HINGE-analyses/blob/master/HINGE_pipeline_NCTC.ipynb) notebook.


![results](results_appeal.png)
