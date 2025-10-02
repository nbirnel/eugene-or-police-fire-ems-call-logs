#!/bin/sh

# USAGE: $0 [epd|spd][/SUBFOLDER] >OUTPUT.csv
dir="$1"

sed 1q "$(find "$dir" -type f -iname '*.csv' -print -quit)"
grep \
  -rh \
  -e 'Accident, Bike' \
  -e 'Accident, Train Injury' \
  -e 'Accident, Vehicle-Bike' \
  -e 'Accident, Vehicle-Pedestrian' \
  -e 'ATL Drunk Driver' \
  -e 'Bike Skateboard Complaint' \
  -e 'Blocked Alley' \
  -e 'Blocked Driveway' \
  -e 'Blocked Sidewalk' \
  -e 'Careless Driving' \
  -e 'Disabled Vehicle(s)' \
  -e 'Driving Complaint' \
  -e 'Driving While Suspended' \
  -e 'DUII' \
  -e 'Hit & Run' \
  -e 'Illegal Motorcycle(s)' \
  -e 'Illegal Motorcycle(s)' \
  -e 'Impound Vehicle(s)' \
  -e 'Missing Vehicle' \
  -e 'Motor Vehicle Injury' \
  -e 'Motor Vehicle No Injury' \
  -e 'Motor Vehicle Unknown' \
  -e 'Railroad Crossing Problem' \
  -e 'Reckless Driving' \
  -e 'Road Closure' \
  -e 'Sign Down' \
  -e 'Speeding Motorcycle(s)' \
  -e 'Speeding Vehicle(s)' \
  -e 'Stop Sign Down' \
  -e 'Storage on Street' \
  -e 'Suspicious Vehicle(s)' \
  -e 'Switched Plates' \
  -e 'Theft from Vehicle' \
  -e 'Towed Vehicle' \
  -e 'Traffic Complaint' \
  -e 'Traffic Hazard' \
  -e 'Traffic Signal Malfunction' \
  -e 'Traffic Stop' \
  -e 'Truck/Safety Checks' \
  -e 'Unauthorized Use of Vehicle' \
  -e 'Unlawful Vehicle Entry' \
  -e 'Wrong Way Driver' \
  "$dir"
