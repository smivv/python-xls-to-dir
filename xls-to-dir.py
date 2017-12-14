import os
import os.path as p

f = open('C:\\Users\\Conf\\PycharmProjects\\python-xls-to-dir\\categories.txt', 'r')
lines = f.readlines()
f.close()

DIR = p.join(p.dirname(p.realpath(__file__)), 'OFR_')

for i, line in enumerate(lines):
    line = line.rstrip()
    if line == '':
        continue
    category = line.split('\t')[0]
    subcategory = line.split('\t')[1]
    if not os.path.exists(p.join(DIR, category)):
        os.mkdir(p.join(DIR, category))
    if not os.path.exists(p.join(DIR, category, subcategory)):
        os.mkdir(p.join(DIR, category, subcategory))