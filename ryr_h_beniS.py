from pymol import cmd
from time import time
import rotkit
from pymol import cmd
cmd.reinitialize()

def mutate( cmd, patho):

    h = 1


    for r,t in patho:
        T1 = time()
        protname = cmd.get_names()[0]
        print("protname :"+protname)
        MutList = [[protname,"A"]]
        for p,c in MutList:
            print (c)
            T = time()
            rotkit.mutate(p, chain=c, resi=r, target=t, mutframe=1)
            print (time() - T)
            cmd.select("%s%s%s"%(p,c,r),"/%s//%s/%s"%((p,c,r)))
            filename="C:/Users/User/OneDrive/Documents/Mutaion/OutputFiles/"+protname+"_"+str(r)+"_"+str(t)+"_"+str(h)+".pdb"
            cmd.save(filename, protname)
            #?cmd.select("name CA")
            #?cmd.save(filename, "sele")
            print (h)
            h=h+1
            print (time() - T1)
        #cmd.reinitialize()

