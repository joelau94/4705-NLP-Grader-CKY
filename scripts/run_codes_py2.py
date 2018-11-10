"""Assuming PYTHONPATH == ROOT
ROOT
  |- scripts
    |- run_codes_py2.py
    |- eval_parser_py2.py
  |- data
    |- parse_dev.dat
    |- parse_dev.key
    |- (status.csv)
  |- py2
"""

import glob
import os
import re
import shutil
import sys
import time


class Status(object):
  def __init__(self, uni):
    # 10 fields
    self.uni = uni
    self.q4_time = -1
    self.q4_success = 0
    self.q5_time = -1
    self.q5_fscore = 0
    self.q5_success = 0
    self.q6_time = -1
    self.q6_fscore = 0
    self.q6_success = 0
    self.has_readme = 0

  def __str__(self):
    return ','.join(map(str, [
        self.uni,
        self.q4_time, self.q4_success,
        self.q5_time, self.q5_fscore, self.q5_success,
        self.q6_time, self.q6_fscore, self.q6_success,
        self.has_readme
    ]))


def run_code(uni, log):
  os.chdir(uni)
  status = Status(uni)

  # students not submitting count_cfg_freq.py or wrong python version
  shutil.copy('../../scripts/count_cfg_freq_py2.py', 'count_cfg_freq.py')

  try:
    q4_start = time.time()
    os.system('python parser.py q4 ../../data/parse_train.dat '
              'parse_train.RARE.dat')
    q4_end = time.time()
    status.q4_time = q4_end - q4_start
    status.q4_success = 1
  except:
    status.q4_success = 0

  try:
    q5_start = time.time()
    os.system('python parser.py q5 parse_train.RARE.dat '
              '../../data/parse_dev.dat q5_prediction_file')
    q5_end = time.time()
    status.q5_time = q5_end - q5_start

    os.system('python ../../scripts/eval_parser_py2.py '
              '../../data/parse_dev.key '
              'q5_prediction_file > q5_eval.txt')
    raw = open('q5_eval.txt', 'r').read()
    res = re.findall(r'total\s+\d+\s+\d+\.\d+\s+\d+\.\d+\s+(\d+\.\d+)', raw)
    if len(res) == 1:
      status.q5_fscore = res[0]
      status.q5_success = 1
  except:
    status.q5_success = 0

  try:
    os.system('python parser.py q4 ../../data/parse_train_vert.dat '
              'parse_train_vert.RARE.dat')

    q6_start = time.time()
    os.system('python parser.py q6 parse_train_vert.RARE.dat '
              '../../data/parse_dev.dat q6_prediction_file')
    q6_end = time.time()
    status.q6_time = q6_end - q6_start

    os.system('python ../../scripts/eval_parser_py2.py '
              '../../data/parse_dev.key '
              'q6_prediction_file > q6_eval.txt')
    raw = open('q6_eval.txt', 'r').read()
    res = re.findall(r'total\s+\d+\s+\d+\.\d+\s+\d+\.\d+\s+(\d+\.\d+)', raw)
    if len(res) == 1:
      status.q6_fscore = res[0]
      status.q6_success = 1
  except:
    status.q6_success = 0

  # not using os.path.exists because a lot of students
  # are not strictly following instructions on cases
  fnames = map(lambda s: s.lower(), glob.glob('*'))
  if 'readme.txt' in fnames:
    status.has_readme = 1

  log.write(str(status) + '\n')

  os.chdir('../')


def run_all_codes(log):
  os.chdir('py2')
  uni_dirs = [pathname for pathname in os.listdir('.')
              if os.path.isdir(pathname)]
  for uni in uni_dirs:
    run_code(uni, log)


def main():
  log = open(sys.argv[1], 'a+')  # status.csv
  run_all_codes(log)


if __name__ == '__main__':
  main()
