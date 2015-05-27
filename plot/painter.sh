#!/bin/bash

TYPE=$1
INPUT=$2
OUTPUT=$3

SED_INPUT_REPLACE="s|INPUT|${INPUT}|g"
SED_OUTPUT_REPLACE="s|OUTPUT|${OUTPUT}|g"

cp ${TYPE}.gnuplot tmp.gnuplot
sed -i $SED_INPUT_REPLACE tmp.gnuplot
sed -i $SED_OUTPUT_REPLACE tmp.gnuplot
gnuplot tmp.gnuplot
rm tmp.gnuplot
