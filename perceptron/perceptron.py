#!/usr/bin/env python
# coding: utf-8

from sys import argv, exit
from fileutils import read_file, list_files, get_data_sets
from random import shuffle
from os import listdir
from collections import Counter

class Perceptron():
    def __init__(self, alpha):
        self.alpha = alpha
        self.w = {}
        self.tp = 0.
        self.tn = 0.
        self.fp = 0.
        self.fn = 0.

    def calc_p(self, words):
        freq = Counter(words)
        p = 0.
        for word in freq:
            if not word in self.w:
                self.w[word] = 0.
            p += freq[word] * self.w[word]
        return p, freq

    def train(self, words, category):
        c = float(category)
        p, freq = self.calc_p(words)
        if c * p <= 0:
            for word in freq:
                self.w[word] += self.alpha * c * freq[word]
            return False
        return True

    def test(self, filename, category):
        c = float(category)
        p, freq = self.calc_p(filename)
        if p <= 0:
            if category == -1:
                self.tn += 1
            else:
                self.fn += 1
        else:
            if category == 1:
                self.tp += 1
            else:
                self.fp += 1

    def train_and_test(self, ds1, ds2):
        i = 0
        success = 0.
        shuffle(ds1)
        while success * 100. / len(ds1) < 100. and i < 10000:
            success = 0
            for f in ds1:
                if self.train(f[0], f[1]):
                    success += 1
            i += 1
        for f in ds2:
            self.test(f[0], f[1])

    def get_results(self):
        precision = self.tp / (self.tp + self.fp)
        recall = self.tp / (self.tp + self.fn)
        f1 = 2 * ((precision * recall) / (precision + recall))
        return precision, recall, f1

    def print_results(self):
        precision, recall, f1 = self.get_results()
        print "Precision:", precision
        print "Recall:", recall
        print "F1:", f1


def usage():
    print argv[0], "<data set>"
    exit(1)

if __name__ == '__main__':
    if len(argv) < 2:
        usage()

    try:
        ds1, ds2 = get_data_sets(argv[1])
    except:
        print 'invalid data set'
        exit(1)

    p = Perceptron(.25)
    p.train_and_test(ds1, ds2)
    p.print_results()
