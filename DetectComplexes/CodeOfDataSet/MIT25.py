import xml.etree.ElementTree as ET
root = ET.parse('DataSets\dip20170205.mif25').getroot()
max=0
# for child in root:
#     for child1 in child:
#         for child2 in child1:
#             print(child2)
a=set()
protienLables=set()
for type_tag in root.findall('{http://psi.hupo.org/mi/mif}entry/{http://psi.hupo.org/mi/mif}interactorList/{http://psi.hupo.org/mi/mif}interactor'):

    # name=type_tag.find("{http://psi.hupo.org/mi/mif}names")
    # if(name.find("{http://psi.hupo.org/mi/mif}shortLabel")!=None):
    #     a=name.find("{http://psi.hupo.org/mi/mif}shortLabel")
    #     for child in type_tag:
    #         if(child.tag=="{http://psi.hupo.org/mi/mif}interactorType"):
    #             for child1 in child:
    #                 if(child1.tag=="{http://psi.hupo.org/mi/mif}names"):
    #                     for child2 in child1:
    #                         if (child2.tag == "{http://psi.hupo.org/mi/mif}fullName"):
    #                             if(child2.text=="protein"):
    #                                 value = type_tag.get('id')
    #                                 print(value)
    #                                 # if(int(value)>max):
    #                                 #     max=int(value)
    #                                 max+=1

    organism=type_tag.find("{http://psi.hupo.org/mi/mif}organism")
    names=organism.find("{http://psi.hupo.org/mi/mif}names")
    fullName = names.find("{http://psi.hupo.org/mi/mif}fullName")
    shortLabel=names.find("{http://psi.hupo.org/mi/mif}shortLabel")
    if shortLabel!= None :
        # if(fullName.text not in a):
        #     a.add(fullName.text)
        #     print(fullName.text)
    #     if(fullName.text=="baker's yeast"):
    #         proteinName=type_tag.find("{http://psi.hupo.org/mi/mif}names")
    #         shortLabel=proteinName.find("{http://psi.hupo.org/mi/mif}fullName")
    #         protienLables.add(shortLabel.text)
    # elif shortLabel!= None:
        if shortLabel.text=="Saccharomyces cerevisiae":
            proteinName = type_tag.find("{http://psi.hupo.org/mi/mif}names")
            shortLabel = proteinName.find("{http://psi.hupo.org/mi/mif}fullName")
            protienLables.add(shortLabel.text)

    else:
        print(type_tag.get("id"))
        max+=1

print("num =%d" %len(protienLables))
print("max =%d" %max)

#*****************************************************************************
# a=set()
# for type_tag in root.findall('{http://psi.hupo.org/mi/mif}entry/{http://psi.hupo.org/mi/mif}interactionList/{http://psi.hupo.org/mi/mif}interaction'):
#     type=type_tag.find("{http://psi.hupo.org/mi/mif}interactionType")
#     name=type.find("{http://psi.hupo.org/mi/mif}names")
#     fullName=name.find("{http://psi.hupo.org/mi/mif}fullName")

    # if(fullName.text== "physical association"):
    #     experimentList=type_tag.find("{http://psi.hupo.org/mi/mif}experimentList")
    #     for experiment in experimentList.findall("{http://psi.hupo.org/mi/mif}experimentDescription"):
    #         name = 0
    #         attributeList=experiment.find("{http://psi.hupo.org/mi/mif}attributeList")
    #         for attribute in attributeList.findall("{http://psi.hupo.org/mi/mif}attribute"):
    #             if(attribute.get("name")=="dip:evidence-for-name"):
    #                 if(attribute.text=="physical interaction"):
    #                     name=1
    #         if(name==1):
    #             for attribute in attributeList.findall("{http://psi.hupo.org/mi/mif}attribute"):
    #                 if (attribute.get("name") == "dip:evidence-scale-name"):
    #                     if (attribute.text != "high throughput"):
    #                         print(attribute.text)
    #                         max+=1

#*****************************************************************************************
    # if(name.find("{http://psi.hupo.org/mi/mif}shortLabel")!=None):
    #     a=name.find("{http://psi.hupo.org/mi/mif}shortLabel")
    #     for child in type_tag:
    #         if(child.tag=="{http://psi.hupo.org/mi/mif}interactorType"):
    #             for child1 in child:
    #                 if(child1.tag=="{http://psi.hupo.org/mi/mif}names"):
    #                     for child2 in child1:
    #                         if (child2.tag == "{http://psi.hupo.org/mi/mif}fullName"):
    #                             if(child2.text=="protein"):
    #                                 value = type_tag.get('id')
    #                                 print(value)
    #                                 # if(int(value)>max):
    #                                 #     max=int(value)
    #                                 max+=1

#*************************************************************************************
#     if(fullName.text not in a):
#         a.add(fullName.text)
#         print(fullName.text)
#
# for i in a:
#     print(i)
#     m=0
#     for type_tag in root.findall('{http://psi.hupo.org/mi/mif}entry/{http://psi.hupo.org/mi/mif}interactionList/{http://psi.hupo.org/mi/mif}interaction'):
#         type=type_tag.find("{http://psi.hupo.org/mi/mif}interactionType")
#         name=type.find("{http://psi.hupo.org/mi/mif}names")
#         fullName=name.find("{http://psi.hupo.org/mi/mif}fullName")
#         if(fullName.text==i):
#             m+=1
#     print(m)



# print("max =%d" %max)