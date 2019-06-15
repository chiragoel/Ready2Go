import random as r
fw = open("input.csv","w")
a= "Class"
for i in range(100):
    col = "F" + str(i+1) +","
    fw.write(col)
classy = "%s \n"%(a)
fw.write(classy)


for j in range(1000):
    
    for i in range(100):
        wr = round(r.uniform(40,260),0)
        writ = "%s , "%(str(wr))
        fw.write(writ)
    cl = r.randint(0,1)
    clas = "%s \n"%(str(cl))
    fw.write(clas)
    
    
fw.close()