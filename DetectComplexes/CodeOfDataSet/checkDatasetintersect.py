import Adress

def f():
    cyc=set()
    linelist=set()
    with open(Adress.adress+"DataSets\\cyc.txt", "r") as file:
        for line in file:
            linelist.add(line)
            a=line.split()
            for i in a:
                cyc.add(i.strip())

    sourceDataSet=set()
    # with open(Adress.adress+"DataSets\\krogan2006_core.txt", "r") as f1:
    with open(Adress.adress+"DataSets\\DIP_ProteinName.txt", "r") as f1:
        for line in enumerate(f1):
            sourceDataSet.add(line[1].split()[0].strip())
            sourceDataSet.add(line[1].split()[1].strip())

    deleted=set()
    for i in cyc:
        if i not in sourceDataSet:
            deleted.add(i)

    print(len(deleted))


    print(len(linelist))

    linelist2=[]
    z=0
    print(deleted)


    for line in linelist:
        for i in deleted:
            if i+" " in line:
                line=line.replace(i,"")
        line=line.strip()
        if(line!="" and len(line.split())>2):
            linelist2.append(line+"\n")

        # if(line!="" ):
        #     linelist2.append(line+"\n")
    last=linelist2[len(linelist2)-1]
    linelist2.pop()
    linelist2.append(last[0:len(last)-1])
    print(len(linelist2))


    f2 = open(Adress.adress+"DataSets\cyc2.txt", 'w')
    f2.writelines(linelist2)
    f2.close()


    newCyc=set()
    with open(Adress.adress+"DataSets\cyc2.txt", "r") as file:
        for line in file:
            a=line.split()
            for i in a:
                newCyc.add(i.strip())

    deleted = set()
    for i in newCyc:
        if i not in sourceDataSet:
            deleted.add(i)

    print(len(deleted))

f()