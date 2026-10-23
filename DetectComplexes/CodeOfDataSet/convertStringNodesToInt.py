import csv
import pickle
import Adress


# this class use for convert String Nodes to int and save them in pickle.

# read dataset***********************************************
file=open( Adress.adress+"DataSets\\krogan2006_core.csv", "r")
reader = csv.reader(file)

#  read Nodes and save in a list************************************
listNodesName=[]
for line in reader:
    listNodesName.append(line[0])
    listNodesName.append(line[1])

#  unique nodes name*****************************************
y=list(sorted(set(listNodesName),key=listNodesName.index))  #sorted for that do not sort  the input by set ******
print(len(y))

#  save nodes in a dictionary and convert to int ************************
dictConvertToInt={}
i=0
for i in range(len(y)):
    dictConvertToInt[y[i]]=str(i)

# save dictionary in a pickle file******************************************

with open(Adress.adress+'PickleData\convert_to_int_krogan2006_core.pickle', 'wb') as handle:
    pickle.dump(dictConvertToInt, handle, protocol=pickle.HIGHEST_PROTOCOL)


# read and print dictionary from pickle file ****************************************

with open(Adress.adress+'PickleData\convert_to_int_krogan2006_core.pickle', 'rb') as handle:
    b = pickle.load(handle)
for x, y in b.items():
  print(x,y)

#  convert to int and save in file *************************************************

# fileIn=open("DataSets\dip20170205_python.CSV", "r")
# fileOut=open('DataSets\dip_output.txt', 'w')
# r = csv.reader(fileIn)
# w = csv.writer(fileOut)
#
# for line in r:
#     str=""
#     for item in enumerate(line):
#         p1=dictConvertToInt[item[1]]
#         str+=p1+" "
#     fileOut.write(str+"\n")

