#!/usr/bin/env python

import sys
from csvtools import *

plot = [float_table,
        take_columns([0]),
        map_column(0, int),
        compute_deltacolumn(0)]

if __name__ == '__main__':
    save_csv(execute_operations(read_csv(sys.argv[1]), plot),
             sys.argv[2])
