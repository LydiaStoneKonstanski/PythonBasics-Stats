#!/usr/bin/env bash

# Run this file from Terminal using ./runTests.sh
files=*.csv
echo "Data sets:", $files
echo
echo "Run IO test"
echo
python3 test_io.py $files
echo
echo "Run Tests"
echo
python3 test_stats.py $files