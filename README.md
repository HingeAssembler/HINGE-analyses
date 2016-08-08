# HINGE-analyses
Analysis accompanying  "HINGE: Long-Read Assembly Achieves Optimal Repeat Resolution" http://biorxiv.org/content/early/2016/07/05/062117


This repository provides an analysis pipeline that reproduces the main results in the paper step-by-step.


###Requirements

The following software needs to be installed (and can be installed using apt-get).

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

Most of these can be installed with apt-get. [Cmake 3.2](http://askubuntu.com/questions/610291/how-to-install-cmake-3-2-on-ubuntu-14-04) can be installed from this ppa on ubuntu: ` ppa:george-edison55/cmake-3.x` on ubuntu, and [gcc/g++-4.9](http://askubuntu.com/questions/428198/getting-installing-gcc-g-4-9-on-ubuntu) from `ppa:ubuntu-toolchain-r/test`.



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

The python packages installed by the last line are the following. 


-  [numpy](https://pypi.python.org/pypi/numpy)
-  [ujson](https://pypi.python.org/pypi/ujson)
-  [cython](https://pypi.python.org/pypi/Cython/)
-  [networkx](https://pypi.python.org/pypi/networkx/)
-  [matplotlib](https://pypi.python.org/pypi/matplotlib/)
-  [biopython](https://pypi.python.org/pypi/biopython/1.67)
-  [bcbio-gff](https://pypi.python.org/pypi/bcbio-gff/0.6.2)
-  [bcbio-nextgen](https://pypi.python.org/pypi/bcbio-nextgen/0.9.9)
-  [colormap](https://pypi.python.org/pypi/colormap)
-  [easydev](https://pypi.python.org/pypi/easydev/0.9.25)
-  [forceatlas2](https://pypi.python.org/pypi/ForceAtlas2/1.0)


All of these packages can be alternatively installed with `sudo pip install <package>`. While installing forceatlas2, one should make sure that the code is cython compiled to get a 10x improvement in speed.

We also need [Aspera connect](http://downloads.asperasoft.com/en/downloads/8?list) to speed up the downloads.

The results of Figure 2 in the paper can be reproduced using [this](https://github.com/govinda-kamath/HINGE-analyses/blob/master/HINGE_pipeline_NCTC.ipynb) notebook.


![results](results_appeal.png)
