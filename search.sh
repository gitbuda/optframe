#!/bin/bash

FOLDER=$1
FILES=${FOLDER}/*

for file_name in $FILES
do
    echo $file_name
    ./executor.py -c $file_name
done
