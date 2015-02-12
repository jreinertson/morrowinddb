outp = open("items.csv","w")
inp = open("itemshtml.txt","r")
outp.write("itemID,name\n")
count = 0;
for line in inp:
    if (count == 6):
        count = 0
    if (count == 1):
        idstr = line[18:-6]
        idstr = idstr.replace(",","")
    if (count == 2):
        namstr = line[18:-6]
        namstr = namstr.replace(",","")
        outp.write(idstr + "," + namstr + "\n")
    count = count + 1
   
outp.close()
inp.close()