#!/usr/bin/env python

import csv
import datetime
import math

def read_csv(csv_file_name):
    with open(csv_file_name, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        return [row for row in csvreader]

def save_csv(table, csv_file_name):
    with open(csv_file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in table:
            csvwriter.writerow(row)

def float_table(table):
    return map(lambda row: map(float, row), table)

def compute_deltacolumn(column):
    def diff_rows((a, b)):
        return a + [abs(b[column] - a[column])]

    def curry(table):
        first_row = table[0] + [0]
        return [first_row] + map(diff_rows, zip(table[1:], table))

    return curry

def map_column(column, f):
    def map_row(row):
        new_row = list(row)
        new_row[column] = f(new_row[column])
        return new_row

    def curry(table):
        return map(map_row, table)

    return curry

def filter_by_column(column, p):
    def curry(table):
        return filter(lambda row: p(row[column]), table)

    return curry

def take_columns(columns):
    def curry(table):
        return map(lambda row: map(lambda i: row[i], columns), table)
    return curry

def execute_operations(table, operations):
    result = table
    for op in operations:
        result = op(result)
    return result

def transform_csv_file(input_file_name, operations, output_file_name):
    save_csv(execute_operations(read_csv(input_file_name),
                                operations),
             output_file_name)

pick_distance = [float_table,
                 compute_deltacolumn(0),
                 filter_by_column(2, lambda x: x >= 5.0),
                 compute_deltacolumn(0),
                 map_column(3, lambda x: x / 60.0),
                 take_columns([0, 2, 3]),
                 map_column(0, datetime.datetime.fromtimestamp)]

plot = [float_table,
        take_columns([0]),
        map_column(0, int),
        compute_deltacolumn(0)]
