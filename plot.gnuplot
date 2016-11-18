#!/usr/bin/env gnuplot

set datafile separator ","
set xdata time
set timefmt "%s"
set format x "%H:%M:%S"
set term png size 1920, 1080
set output outfile
plot infile u 1:2 w line
