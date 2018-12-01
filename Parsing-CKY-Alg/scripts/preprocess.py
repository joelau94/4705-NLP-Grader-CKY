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


PY2_DIR = 'py2'
PY3_DIR = 'py3'


def rename_zipfile(filename, py_version):
  file_info = filename.split('_')
  py_version = file_info[-2]
  uni = file_info[-3]


def separate_py_version(all_submissions):
  if not os.path.exists(all_submissions):
    print('Illegal file path: {}'.format(all_submissions))
    return

  os.system('unzip {}'.format(all_submissions))

  if not os.path.exists(PY2_DIR):
    os.mkdir(PY2_DIR)
  if not os.path.exists(PY3_DIR):
    os.mkdir(PY3_DIR)

  zipfile_names = glob.glob('*.zip')

  for filename in zipfile_names:
    if filename == all_submissions:
      continue

    file_info = filename.split('_')
    if len(file_info) <= 3 \
            or not len(re.findall('py[2|3]', file_info[-2])) == 1 \
            or not len(re.findall('\D+\d+', file_info[-3])) == 1:
      print('Illegal file: {}'.format(filename))
      continue

    uni = file_info[-3]
    py_version = file_info[-2]

    if py_version == 'py2':
      shutil.move(filename, os.path.join(PY2_DIR,
                                         '{}_{}_HW3.zip'.format(uni, 'py2')))
    elif py_version == 'py3':
      shutil.move(filename, os.path.join(PY3_DIR,
                                         '{}_{}_HW3.zip'.format(uni, 'py3')))


def extract_zipfile(filename):
  uni, _, _ = filename.split('_')
  os.system('unzip {} -d {}'.format(filename, uni))
  
  os.chdir(uni)

  contents = glob.glob('*')
  if 'parser.py' in contents:
    pass
  elif len(contents) == 1:
    os.system('mv {}/* .'.format(contents[0]))
  elif len(contents) == 2 and '__MACOSX' in contents:
    contents.remove('__MACOSX')
    os.system('mv {}/* .'.format(contents[0]))
  else:
    print('Unknown Error for file {}'.format(filename))

  os.chdir('../')


def extract_all_zipfiles(py_dir):
  os.chdir(py_dir)

  zipfile_names = glob.glob('*.zip')
  for filename in zipfile_names:
    extract_zipfile(filename)

  os.chdir('../')


def main():
  all_submissions = sys.argv[1]
  separate_py_version(all_submissions)
  extract_all_zipfiles(PY2_DIR)
  extract_all_zipfiles(PY3_DIR)


if __name__ == '__main__':
  main()
