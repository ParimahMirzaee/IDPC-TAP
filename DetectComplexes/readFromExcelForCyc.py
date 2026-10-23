import xlrd

workbook = xlrd.open_workbook('DataSets\CYC2008_complex.xls')
sh=workbook.sheet_by_name("DataSets\CYC2008_complex")
print(sh.nrows)
print (sh.ncols)
n=0
i=0

first=sh.cell_value(0,2)
data=""
file=open("DataSets\cyc.txt","w")
for n in range(sh.nrows):
   # آخری باید بدون \n باشد

    if(n==1919):
        data = data + (sh.cell_value(n, 0) + " ")
        print(data)
        file.write(data + " ")

     # دز دو if بعدی چک می کند که آیا کمپلکس عوض می‌شود یا نه ؟

    elif(sh.cell_value(n,2) == first):
        data=data+(sh.cell_value(n,0)+" ")
    else:
        first=sh.cell_value(n,2)
        print(data)
        file.write(data+" ")
        file.write("\n")
        data=""
        data=data+(sh.cell_value(n, 0) + " ")


