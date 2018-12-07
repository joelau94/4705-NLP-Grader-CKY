"""Assuming PYTHONPATH == ROOT
ROOT
  |- scripts
    |- grader.py
  |- data
    |- status.csv
    |- (grades.csv)
"""

import sys


FULL_MARK = 100


def grade(status):
  """
  Status fields:
  'uni', 
  'dev1_uas',
  'dev1_las',
  'dev2_uas',
  'dev2_las',
  'dev3_uas',
  'dev3_las',
  'test1_uas',
  'test1_las',
  'test2_uas',
  'test2_las',
  'test3_uas',
  'test3_las'
  """
  points = FULL_MARK

  # dev uas / las
  if status[1] < 70 or status[3] < 70 or status[5] < 70 or \
          status[2] < 70 or status[4] < 70 or status[6] < 70:
    points -= 20
  elif status[1] < 78 or status[3] < 78 or status[5] < 78 or \
          status[2] < 75 or status[4] < 75 or status[6] < 75:
    points -= 10
  elif status[1] < 82 or status[3] < 82 or status[5] < 82 or \
          status[2] < 78 or status[4] < 78 or status[6] < 78:
    points -= 5

  # test uas / las
  if status[7] < 70 or status[9] < 70 or status[11] < 70 or \
          status[8] < 70 or status[10] < 70 or status[12] < 70:
    points -= 20
  elif status[7] < 78 or status[9] < 78 or status[11] < 78 or \
          status[8] < 75 or status[10] < 75 or status[12] < 75:
    points -= 10
  elif status[7] < 82 or status[9] < 82 or status[11] < 82 or \
          status[8] < 78 or status[10] < 78 or status[12] < 78:
    points -= 5

  # dev-test variance
  # part 1
  if status[1] - status[7] > 1.2 or status[2] - status[8] > 1.2:
    points -= 3
  elif status[1] - status[7] > 3 or status[2] - status[8] > 3:
    points -= 6
  # part 2
  if status[3] - status[9] > 1.2 or status[4] - status[10] > 1.2:
    points -= 3
  elif status[3] - status[9] > 3 or status[4] - status[10] > 3:
    points -= 6
  # part 3
  if status[5] - status[11] > 1.2 or status[6] - status[12] > 1.2:
    points -= 3
  elif status[5] - status[11] > 3 or status[6] - status[12] > 3:
    points -= 6

  # relative improvement
  if status[1] > status[3] or status[2] > status[4] or \
          status[7] > status[9] or status[8] > status[10]:  # part 2 over 1
    points -= 3
  if status[1] > status[5] or status[2] > status[6] or \
          status[7] > status[11] or status[8] > status[12]:  # part 3 over 1
    points -= 3
  if status[3] > status[5] or status[4] > status[6] or \
          status[9] > status[11] or status[10] > status[12]:  # part 3 over 2
    points -= 3

  points = max(0, points)

  status.append(str(points))
  return status


def grade_all(fstat, fgrade):
  for line in fstat:
    status = line.strip().split(',')
    scores = map(float, status[1:])
    status = [status[0]] + scores
    status = grade(status)
    fgrade.write(','.join(map(str, status)) + '\n')


def main():
  fstat = open(sys.argv[1], 'r')  # status.csv
  fgrade = open(sys.argv[2], 'w')  # grades.csv
  grade_all(fstat, fgrade)


if __name__ == '__main__':
  main()
