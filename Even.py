import xlrd #Reads xlsx files
import openpyxl # Writes to xlsx files
import csv #Reads and writes to csv files
import codecs #For decoding
from csv import DictReader #Opens csv as dictionary

def bkn(fname, idx=0): #Opens workbook and the first sheet.
    xl_workbook = xlrd.open_workbook(fname)
    xl_sheet = xl_workbook.sheet_by_index(0)
    return xl_sheet

s1 = bkn('AssetsComparison.xlsx')
s2 = bkn('AssetsExport3.xlsx')

def wrn(file1, file2): #Converts from xlsx to csv.
    with open(file1, 'wb') as conv:
        conv_write = csv.writer(conv)
        for row in range(file2.nrows):
            conv_write.writerow(
            list(x.encode('utf-8')
            if type(x) == type(' ')
            else x for x in file2.row_values(row)))

f1 = wrn('Convert1.csv', s1) #Excel file converted to csv
f2 = wrn('Convert2.csv', s2) #Excel file converted to csv
             #csv_1  #csv_2, #output.csv
def csv_sets(fname1, fname2, outname):
    with codecs.open(fname1, "r", "utf-8-sig") as f:
        reader1 = [row['Address'] for row in DictReader(f)]   #Opens desired row and writes to set
        set1 = set(reader1)
    with codecs.open(fname2, "r", "utf-8-sig") as f2:
        reader2 = [row['Address'] for row in DictReader(f2)]  #Opens desired row and writes to set
        set2 = set(reader2)
    with codecs.open(outname, "wb", "utf-8-sig") as out_f: # writes the diffrence to a new output.csv
        filewriter = csv.writer(out_f)
        for row in set1:
            if row in set2:
                filewriter.writerow([row])
    wb_1 = openpyxl.Workbook() #Creates New Excel File and Sheet
    ws_1 = wb_1.active
    fout = open(outname)  #Opens the output.csv
    reader = csv.reader(fout, delimiter=',')
    for row in reader: #Converts output.csv to output.xlsx
        ws_1.append(row)
    wb_1.save(outname)

c1 = csv_sets('Convert1.csv', 'Convert2.csv', 'FINISHED.xlsx')
