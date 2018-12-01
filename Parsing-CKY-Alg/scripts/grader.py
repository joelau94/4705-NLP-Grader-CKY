"""Assuming PYTHONPATH == ROOT
ROOT
  |- scripts
    |- grader.py
  |- data
    |- status.csv
    |- grades.csv
"""

import sys


FULL_MARK = 80


def grade(status):
  """
  Status fields:
  uni, q4_time, q4_success, q5_time, q5_fscore, q5_success,
  q6_time, q6_fscore, q6_success, has_readme
  """
  points = FULL_MARK

  # q4
  if status[2] == '1':  # q4_success
    q4_time = float(status[1])
    if q4_time > 20:
      points -= 3
    elif q4_time > 10:
      points -= 2
    elif q4_time > 5:
      points -= 1

  else:
    points -= 20

  # q5
  if status[5] == '1':  # q5_success
    q5_time = float(status[3])
    if q5_time > 180:
      points -= 3
    elif q5_time > 120:
      points -= 2
    elif q5_time > 90:
      points -= 1

    q5_fscore = float(status[4])
    if q5_fscore < 0.5:
      points -= 20
    elif q5_fscore < 0.6:
      points -= 10
    elif q5_fscore < 0.7:
      points -= 5
    elif q5_fscore < 0.71:
      points -= 2

  else:
    points -= 40

  # q6
  if status[8] == '1':  # q6_success
    q6_time = float(status[6])
    if q6_time > 300:
      points -= 3
    elif q6_time > 180:
      points -= 2
    elif q6_time > 150:
      points -= 1

    q6_fscore = float(status[7])
    if q6_fscore < 0.5:
      points -= 20
    elif q6_fscore < 0.6:
      points -= 10
    elif q6_fscore < 0.71:
      points -= 5
    elif q6_fscore < 0.735:
      points -= 2

  else:
    points -= 40

  # readme
  if status[9] == '0':
    points -= 5

  points = max(0, points)

  status.append(str(points))
  return status


def grade_all(fstat, fgrade):
  for line in fstat:
    status = line.strip().split(',')
    status = grade(status)
    fgrade.write(','.join(status) + '\n')


def main():
  fstat = open(sys.argv[1], 'r')  # status.csv
  fgrade = open(sys.argv[2], 'w')  # grades.csv
  grade_all(fstat, fgrade)


if __name__ == '__main__':
  main()
