# 4705-NLP-Grader-CKY
Auto-grader for COMS4705 NLP homework on CKY Parsing

+ Download submissions from courseworks2 as zip file.

+ Separate them by python version and extract files to correct path with ```scripts/preprocess.py```.

+ Activate virtualenv for python2 / python3.

+ Execute student codes with ```scripts/run_codes_py2.py``` / ```scripts/run_codes_py3.py```. This produces ```status.csv```.

+ Grade execution results with ```scripts/grader.py```, taking in ```status.csv``` and outputting ```grades.csv```.

+ Export gradebook from courseworks2 as a csv file.

+ Update that csv file with ```scripts/update_gradebook.py```. (Note: Fields of csv file are hard-coded in this script.)

+ Import the new gradebook csv file onto courseworks2.
