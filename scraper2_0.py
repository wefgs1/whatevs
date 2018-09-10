import codecs
import csv
import re
import sys
from csv import DictReader
from csv import DictWriter

"""

def nm(UnknownIP_File,Subnet_File):
    pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}')
    full_ip = []
    partial_ip = []
    subnet = []
    final = []
    file1 = open(UnknownIP_File)
    file2 = open(Subnet_File)
    for row in file1:
        full_ip.append(row)
        if re.match(pattern, row):
            partial_ip.append(re.match(pattern, row).group(0))
    for line in file2:
        subnet.append(line)
    for x in full_ip:
        for y in subnet:
            for z in partial_ip:
                if z in y:
                    final.append(x)
                    final.append(y)
    for something in final:
        print(something)
c1 = nm('Failed.txt', 'subnets.txt')


"""


def compare(file1, file2):
    f1 = open(file1)
    f2 = open(file2)
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for line in f1:
        line = line.strip('\r\n')
        l1.append(line)
    for item in f2:
        item = item.strip('\r\n')
        l2.append(item)

    for x in l1:
        x1 = x[:9]
        x2 = x[9:12]
        for y in l2:
            y1 = y[:9]
            y2 = y[14:]
            if x1 in y1:
                #print(x1+x2+ " " + y2)
                l3.append((x1)+(x2)+ (";")+(y2))
                l4.append((x1)+(x2))
    set1 = set(l1)
    set2 = set(l4)
    set3 = set1 | set2

    diff1 = set1 - set2

    #for line in diff1:
        #print(line)
    with codecs.open('Successful.csv', "wb", "utf-8-sig") as f:
        writer = csv.writer(f)
        for line in l3:
            writer.writerow([line])

c2 = compare('Failed.txt','subnets.txt')
