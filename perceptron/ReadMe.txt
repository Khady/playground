Perceptron
============

Author
------

Louis Roché <louis.roche@epitech.eu> 2013400577

Usage
-----

    python perceptron.py <data set>

Example
-------

    $ python perceptron.py "data/data 1"
    Precision: 0.959325396825
    Recall: 0.971859296482
    F1: 0.965551672491

Results
-------

    alpha = 0.25

The average precision, recall and F1 are 0.951, 0.954 and 0.956 for 20 runs.

Code
----

All the perceptron code is in the file ```perceptron.py```. ```fileutils.py``` contains the
code to read and parse the data set.

The main function (in ```perceptron.py```) reads all the files in the data set. For
each file, it will count the frequency of the words. The data are in a
dictionary which has 2 arrays. One for the baseball and one for the hockey.

The arrays are split in two parts to get ds1 and ds2. ds1 uses 4/5 of the data
and ds2 1/5.

Then ds1 is shuffled. The perceptron is trained with ds1. And then ds2 is
tested.
