"""Assuming PYTHONPATH == ROOT
ROOT
  |- scripts
    |- run_eval.py
    |- eval.py
  |- data
    |- dev.conll
    |- test.conll
  |- (status.csv)
  |- hypotheses
"""

import glob
import os
import re
import shutil
import sys
import time


HYP_DIR = 'hypotheses'
PARTS = ['dev1', 'dev2', 'dev3', 'test1', 'test2', 'test3']
REF_FILES = ['../data/dev.conll'] * 3 + ['../data/test.conll'] * 3
HYP_FILES = ['dev_part1.conll', 'dev_part2.conll', 'dev_part3.conll',
             'test_part1.conll', 'test_part2.conll', 'test_part3.conll']


class Status(object):
  def __init__(self, uni):
    # 13 fields
    self.uni = uni
    self.scores = {
        'dev1_uas': 0.,
        'dev1_las': 0.,
        'dev2_uas': 0.,
        'dev2_las': 0.,
        'dev3_uas': 0.,
        'dev3_las': 0.,
        'test1_uas': 0.,
        'test1_las': 0.,
        'test2_uas': 0.,
        'test2_las': 0.,
        'test3_uas': 0.,
        'test3_las': 0.,
    }

  def __str__(self):
    return ','.join(map(str, [
        self.uni,
        self.scores['dev1_uas'], self.scores['dev1_las'],
        self.scores['dev2_uas'], self.scores['dev2_las'],
        self.scores['dev3_uas'], self.scores['dev3_las'],
        self.scores['test1_uas'], self.scores['test1_las'],
        self.scores['test2_uas'], self.scores['test2_las'],
        self.scores['test3_uas'], self.scores['test3_las']
    ]))


def run_eval(uni, log):
  print('Evaluating {} ...'.format(uni))
  status = Status(uni)

  try:
    # check duplicate
    dev1_str = open('{}/dev_part1.conll'.format(uni), 'r').read().strip()
  except:
    dev1_str = uni

  for part, ref, hyp in zip(PARTS, REF_FILES, HYP_FILES):
    try:
      if not os.path.exists('{}/{}'.format(uni, hyp)):
        continue
      os.system('python ../scripts/eval.py {} {}/{} > {}/{}.out'
                .format(ref, uni, hyp, uni, hyp))
      raw = open('{}/{}.out'.format(uni, hyp), 'r').read()
      uas = re.findall(r'Unlabeled attachment score\s+(\d+\.\d+)', raw)
      if len(uas) == 1:
        status.scores[part + '_uas'] = uas[0]
      las = re.findall(r'Labeled attachment score\s+(\d+\.\d+)', raw)
      if len(las) == 1:
        status.scores[part + '_las'] = las[0]
    except:
      pass

  log.write(str(status) + '\n')
  return dev1_str


def run_eval_all(log):
  os.chdir(HYP_DIR)
  uni_dirs = [pathname for pathname in os.listdir('.')
              if os.path.isdir(pathname)]

  dev1_strs = {}

  for uni in uni_dirs:
    dev1_strs[uni] = run_eval(uni, log)
  
  print('Total submissions graded: {}'.format(len(dev1_strs)))
  return dev1_strs


def check_duplicate(strs):
  for uni1 in strs.keys():
    for uni2 in strs.keys():
      if (not uni1 == uni2) and strs[uni1] == strs[uni2]:
        print('Potential duplicate: {}, {}'.format(uni1, uni2))


def main():
  log = open(sys.argv[1], 'a+')  # status.csv
  dev1_strs = run_eval_all(log)
  check_duplicate(dev1_strs)


if __name__ == '__main__':
  main()
