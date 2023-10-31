import csv
with open('innovators.csv','r')as file:
 reader=csv.reader(file,delimeter='\t')
for row in reader:
    print(row)
