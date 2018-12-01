import csv
from collections import defaultdict
import os
import sys


def read_grades(filename):
  fgrade = open(filename, 'r')
  grades = defaultdict(int)
  for line in fgrade:
    entry = line.strip().split(',')
    grades[entry[0]] = int(entry[10])
  return grades


def write_gradebook(grades, in_file, out_file):
  os.system('touch {}'.format(out_file))
  grade_reader = csv.reader(open(in_file, 'r'))
  grade_writer = csv.writer(open(out_file, 'w'))

  for row in grade_reader:
    if row[2] in grades:
      row[9] = str(grades[row[2]])
    grade_writer.writerow(row)


def main():
  grades = read_grades(sys.argv[1])  # grades.csv
  # gradebook.csv, new_gradebook.csv
  write_gradebook(grades, sys.argv[2], sys.argv[3])


if __name__ == '__main__':
  main()
