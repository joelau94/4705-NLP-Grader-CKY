# 4705-NLP-Grader-CKY
Auto-grader for COMS4705 NLP homework on Neural Dependency Parsing

+ Download submissions from courseworks2 as zip file.

+ Extract files to correct path with ```scripts/preprocess.py```.

+ Activate virtualenv for python2 / python3.

+ Evaluate student outputs with ```scripts/run_eval.py```. This produces ```status.csv```.

+ Grade evaluation results with ```scripts/grader.py```, taking in ```status.csv``` and outputting ```grades.csv```.

+ Export gradebook from courseworks2 as a csv file.

+ Update that csv file with ```scripts/update_gradebook.py```. (Note: Fields of csv file are hard-coded in this script.)

+ Import the new gradebook csv file onto courseworks2.
