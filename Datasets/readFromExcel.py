import csv
from collections import defaultdict
import Adress

# columns = defaultdict(list) # each value in each column is appended to a list
#
# with open(Adress.adress+"DataSets\\BIOGRID-MV-Physical-3.4.137.tab2.csv") as f:
#     reader = csv.DictReader(f) # read rows into a dictionary format
#     for row in reader: # read a row as {column1: value1, column2: value2,...}
#         for (k,v) in row.items(): # go over each column name and value
#             if k=="Throughput":
#                 if v=="Low Throughput":
#                     columns[k].append(v)
#             else:
#                 columns[k].append(v) # append the value into the appropriate list
#                                  # based on column name k
#
# print(len(columns['Entrez Gene Interactor A']))
import csv
with open(Adress.adress+"DataSets\\BIOGRID-ALL-3.4.137.csv") as inp, open(Adress.adress+"DataSets\\biogrid.csv", 'w',newline='') as out:
    writer = csv.writer(out)
    i=0
    for row in csv.reader(inp):
        if i==0:
            writer.writerow(row)
        elif row[17] == "Low Throughput" and row[23]=="BIOGRID" and row[5]!="-" and row[6] != "-":
            writer.writerow(row)
        i+=1

