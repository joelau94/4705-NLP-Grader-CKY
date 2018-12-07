"""Assuming PYTHONPATH == ROOT
ROOT
  |- submissions.zip
  |- scripts
    |- preprocess.py
"""

import glob
import os
import re
import shutil
import sys


HYP_DIR = 'hypotheses'


def filter_zipfiles(all_submissions):
  if not os.path.exists(all_submissions):
    print('Illegal file path: {}'.format(all_submissions))
    return

  os.system('unzip {}'.format(all_submissions))

  if not os.path.exists(HYP_DIR):
    os.mkdir(HYP_DIR)

  zipfile_names = glob.glob('*.zip')

  for filename in zipfile_names:
    if filename == all_submissions:
      continue

    file_info = filename.split('_')
    if len(file_info) <= 2 \
            or not len(re.findall('\D+\d+', file_info[-2])) == 1:
      print('Illegal file: {}'.format(filename))
      continue

    uni = file_info[-2]
    shutil.move(filename, os.path.join(HYP_DIR, '{}_HW4.zip'.format(uni)))


def extract_zipfile(filename):
  uni, _ = filename.split('_')
  os.system('unzip {} -d {}'.format(filename, uni))
  
  os.chdir(uni)

  contents = glob.glob('*')
  if 'dev_part1.conll' in contents:
    pass
  elif len(contents) == 1:
    os.system('mv {}/* .'.format(contents[0]))
  elif len(contents) == 2 and '__MACOSX' in contents:
    contents.remove('__MACOSX')
    os.system('mv {}/* .'.format(contents[0]))
  else:
    print('Unknown Error for file {}'.format(filename))

  os.chdir('../')


def extract_all_zipfiles(hyp_dir):
  os.chdir(hyp_dir)

  zipfile_names = glob.glob('*.zip')
  for filename in zipfile_names:
    extract_zipfile(filename)

  os.chdir('../')


def main():
  all_submissions = sys.argv[1]
  filter_zipfiles(all_submissions)
  extract_all_zipfiles(HYP_DIR)


if __name__ == '__main__':
  main()
