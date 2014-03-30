#!/bin/bash

# Recipe and source are stored together
SRC_DIR=$RECIPE_DIR/..
pushd $SRC_DIR

$PYTHON setup.py install --single-version-externally-managed --record=/tmp/record.txt
popd
