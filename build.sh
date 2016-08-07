#!/bin/bash

pwd=$PWD/HINGE
cd $pwd/thirdparty/DAZZ_DB
make clean
make -j 8

cd $pwd/thirdparty//DALIGNER
make clean
make -j 8

cd $pwd/thirdparty/DASCRUBBER
make clean
make -j 8

cd $pwd/thirdparty/DEXTRACTOR
make clean
make -j 8

cd $pwd
rm -rf build
mkdir build
cd $pwd/build
cmake .. -DCMAKE_C_COMPILER=gcc-4.9 -DCMAKE_CXX_COMPILER=g++-4.9
make -j 8

exit $?
