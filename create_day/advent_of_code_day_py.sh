#!/bin/bash

YEAR=""
DAY=""

while getopts y:d: flag
do
    case "${flag}" in
        y) YEAR=${OPTARG};;
        d) DAY=${OPTARG};;
    esac
done

if [ -z "$YEAR" ]; then
    echo "Error: Year (-y) is required."
    exit 1
fi

if [ -z "$DAY" ]; then
    echo "Error: Day (-d) is required."
    exit 1
fi

FORMATTED_DAY=$(printf "%02d" $DAY)
DIR_PATH="${YEAR}/python/day-${FORMATTED_DAY}"
mkdir -p $DIR_PATH

if [ -f create_day/template_code/sol.py ]; then
    cp create_day/template_code/sol.py $DIR_PATH/
else
    echo "Python template file not found. Creating an empty sol.py file."
    touch $DIR_PATH/sol.py
fi

# Create input files
touch $DIR_PATH/input.txt
touch $DIR_PATH/dummy_input.txt

echo "AoC ${YEAR} day ${FORMATTED_DAY} created for python."