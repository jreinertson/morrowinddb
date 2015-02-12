outp = open("itemInsert.sql","w")
inp = open("itemshtml.txt","r")
outp.write("SET search_path TO ItemDB;\n")
count = 0;
for line in inp:
    if (count == 6):
        count = 0
    if (count == 1):
        idstr = line[18:-6]
    if (count == 2):
        namstr = line[18:-6]
        outp.write("INSERT INTO items VALUES(\"" + idstr + "\",\"" + namstr + "\");\n")
    count = count + 1
   
outp.close()
inp.close()