#!/bin/sh

USAGE="$0 SOURCE_DIRECTORY"
src=$1
dest=$1.csv

sed 1q $(find "$src" -type f -iname '*.csv' | sed 1q) >$dest

for csv in $(find "$src" -type f -iname '*.csv' | sort ); do
    sed 1d $csv >>$dest
done

