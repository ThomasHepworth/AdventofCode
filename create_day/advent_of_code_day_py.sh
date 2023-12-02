#!/bin/bash

# Process command-line arguments
while getopts y:d: flag
do
    case "${flag}" in
        y) YEAR=${OPTARG};;
        d) DAY=${OPTARG};;
    esac
done

# Format day with leading zero
FORMATTED_DAY=$(printf "%02d" $DAY)

# Create directory structure
DIR_PATH="${YEAR}/python/day-${FORMATTED_DAY}"
mkdir -p $DIR_PATH

# Copy Python template file if it exists
if [ -f create_day/template_code/sol.py ]; then
    cp create_day/template_code/sol.py $DIR_PATH/
else
    echo "Python template file not found. Creating an empty sol.py file."
    touch $DIR_PATH/sol.py
fi
touch $DIR_PATH/input.txt
touch $DIR_PATH/dummy_input.txt


echo "AoC 2023 day ${DAY} created for python."
