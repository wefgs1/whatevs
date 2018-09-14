import ipaddress
from ipaddress import IPv4Network
from ipaddress import IPv4Address
import codecs
from csv import DictReader
import csv
#file1 = open('IP.txt', 'r')
file2 = open('Subnet.txt', 'r')

ip_list = []
subnet_list = []


def csv_s(fname1):
    with codecs.open(fname1, "r", "utf-8-sig") as f:
        reader1 = [row['Address'] for row in DictReader(f)]
        for line in reader1:
            line = line.strip('\n')
            ip_list.append(line)

compare = csv_s('Unknown OS.csv')

#for line in file1:
#    line = line.strip('\n')
#    ip_list.append(line)
for item in file2:
    subnet_list.append(item)

csv_1 = codecs.open('Identified_Assets.csv', 'wb', 'utf-8-sig')
filewriter = csv.writer(csv_1)
filewriter.writerow(['Address', 'Location', 'Site_Name'])
for line in ip_list:
    ip_a = IPv4Address(unicode(line))
    for item in subnet_list:
        cut_items = item.split('  ', 3)
        subnet_a = IPv4Network(unicode(cut_items[0]))
        if ip_a in subnet_a:
            print(str(ip_a), cut_items[1], cut_items[2])
            filewriter.writerow([str(ip_a), cut_items[1], cut_items[2].strip('\n')])
        else:
            print('Not Identified.')
