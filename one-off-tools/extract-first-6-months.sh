#!/bin/sh


sed 1q "$(find "epd" -type f -iname '*.csv' -print -quit)"

for year in $(seq 2023 2025); do
    for month in 01 02 03 04 05 06; do
        find epd/$year/$month -type f -iname '*csv' -exec sed 1d '{}' ';'
    done
done
