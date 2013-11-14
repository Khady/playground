#!/usr/bin/env python
# coding: utf-8

from os import listdir
from re import split

def list_files(folder):
    files = {'baseball':[], 'hockey':[]}
    for d in listdir(folder):
        if d[0] == '.':
            continue
        for s in listdir("%s/%s/hockey" % (folder, d)):
            if s[0] == '.':
                continue
            files['hockey'].append("%s/%s/hockey/%s" % (folder, d, s))
        for s in listdir("%s/%s/baseball" % (folder, d)):
            if s[0] == '.':
                continue
            files['baseball'].append("%s/%s/baseball/%s" % (folder, d, s))
    return files

def read_file(filename):
    lines = []
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except:
        return []

    words = []
    for l in lines:
        words = words + split('\W+', l)
    clean_words = [x for x in words if x != '' and len(x) > 2 and len(x) < 20]
    return clean_words

def get_data_sets(folder):
    files = list_files(folder)

    words_files_1 = []
    for f in files['baseball'][:4 * len(files['baseball']) / 5]:
        words_files_1.append((read_file(f), -1.))
    for f in files['hockey'][:4 * len(files['hockey']) / 5]:
        words_files_1.append((read_file(f), 1.))

    words_files_2 = []
    for f in files['baseball'][4 * len(files['baseball']) / 5:]:
        words_files_2.append((read_file(f), -1.))
    for f in files['hockey'][4 * len(files['hockey']) / 5:]:
        words_files_2.append((read_file(f), 1.))

    return words_files_1, words_files_2
