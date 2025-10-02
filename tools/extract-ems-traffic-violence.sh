#!/bin/sh



# USAGE: $0 fire-ems/[SUBFOLDER]  >OUTPUT.csv
dir="$1"

sed 1q "$(find "$dir" -type f -iname '*.csv' -print -quit)"
grep \
  -rh \
  -e 'ACCIDENT ATV INJURY' \
  -e 'ACCIDENT BIKE' \
  -e 'ACCIDENT TRAIN INJURY' \
  -e 'ACCIDENT VEHICLE BIKE' \
  -e 'HIT AND RUN INJURY' \
  -e 'MOTOR VEH ACC FATALITY' \
  -e 'MOTOR VEH ACC INJURY' \
  -e 'MOTOR VEH ACC NO INJURY' \
  -e 'MOTOR VEH ACC UNKNOWN INJ' \
  -e 'MOTOR VEHICLE ACC W/HAZMAT' \
  -e 'RAILROAD CROSSING PROBLEM' \
  -e 'TRAIN VS PED/BIKE CRASH' \
  -e 'TRAIN VS VEHICLE CRASH' \
  -e 'VEHICLE/PEDESTRIAN CRASH' \
  -e 'VEHICLE FIRE' \
  "$dir"
