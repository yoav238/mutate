from time import time
import pymolTest
from pymolTest import cmd
import rotkit
cmd.reinitialize()


cmd.load("C:/Users/User/OneDrive/Documents/Mutaion/From rcsb/2cba.pdb")
protname = cmd.get_names()[0]
#molname = cmd.get_names()[1]
print(protname)
patho=[[507 ,'Ile'], [877 ,'Pro'], [1136,'Val'], [1365,'Val'], [1400,'Gly'], [1885,'Glu'], [1886,'Ser'], [2958,'Arg'], [3187,'Arg'], [3461,'Val']]


for r,t in patho:
    h=1
    T1 = time()
	
    cmd.load("C:/Users/User/OneDrive/Documents/Mutaion/From rcsb/2cba.pdb")
    protname = cmd.get_names()[0]
    MutList = [[protname,"A"]]#,[protname,"D"]]
    for p,c in MutList:
        print (c)
        T = time()
        rotkit.mutate(p, chain=c, resi=r, target=t, mutframe=1)
        print (time() - T)
        cmd.select("%s%s%s"%(p,c,r),"/%s//%s/%s"%((p,c,r)))

        filename=("C:/Users/User/OneDrive/Documents/Mutaion/AfterMut/benign"+"_"+str(r)+"_"+str(t)+"_"+str(h)+".pdb")
		cmd.save(filename, protname)
        cmd.select("name CA")
        cmd.save(filename, "sele")
        print (h)
        h=h+1
        print (time() - T1)
    cmd.reinitialize()

