The code is written in python
It runs reliably on linux. 
Windows versions of python should be able to run it, but I haven't tried it yet.
It would also run on online python notebooks such as jupyter notebook

Both the class_SBD.py and class_SBD_test.py files should be in the same directory
so should be the sbd files whose content is to be read.
To see the contents of a file, edit the class_SDB_test.py file at 
line No. 14 where it says:
with open('300434060605980_000319.sbd', 'r') as file:
change that to your sbd file so that it looks like
with open('yourfile.sbd', 'r') as file:

then run python on a command terminal as
python class_SBD_test.py

It should display all the contents
