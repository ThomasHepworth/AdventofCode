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

# Create base directory structure
BASE_DIR_PATH="${YEAR}/rust"
mkdir -p $BASE_DIR_PATH

# Directory for the specific day
DAY_DIR_PATH="${BASE_DIR_PATH}/day-${FORMATTED_DAY}"

# Create a new Rust project
cargo new --lib "${BASE_DIR_PATH}/day-${FORMATTED_DAY}"

# Create input files in the day-specific directory
mkdir -p $DAY_DIR_PATH
mkdir -p $DAY_DIR_PATH/src/bin
touch $DAY_DIR_PATH/input.txt
touch $DAY_DIR_PATH/dummy_input.txt

if [ -f create_day/template_code/sol.rs ]; then
    # Copy Rust template file
    cp create_day/template_code/sol.rs "${BASE_DIR_PATH}/day-${FORMATTED_DAY}/src/bin/"
    # Replace placeholder with actual day
    sed -i '' "s/day_01/day_$FORMATTED_DAY/" "${BASE_DIR_PATH}/day-${FORMATTED_DAY}/src/bin/sol.rs"
else
    echo "Rust template file not found. Creating an empty sol.rs file."
    touch "${BASE_DIR_PATH}/day-${FORMATTED_DAY}/src/bin/sol.rs"
fi

echo "AoC 2023 day ${DAY} created for rust."
