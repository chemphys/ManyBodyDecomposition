
# coding: utf-8

# In[ ]:

import itertools as it
import sys
import os


# In[ ]:

if len(sys.argv) != 3:
    print("Usage: python3 "  + sys.argv[0] + " cluster.xyz" + " mode")
    print("mode=1: no cp")
    print("mode=2, whole cluster cp")
    print("mode=3, individual cluster cp")
    sys.exit(1)
fxyz = sys.argv[1]
mode = int(sys.argv[2])
#fxyz = "cluster.xyz"
atlist = [3,3,3,3,3]
chglist = [0,0,0,0,0]
#mode = 3
#atlist = [3,3]


# In[ ]:

# Function to write the different combinations from an xyz file

def write_combs(xyz, use_cp, atlist):
    f = open(xyz,'r')

    nat = f.readline().split()[0]
    f.readline()
    mons = []
    for i in range(len(atlist)):
        m = []
        for j in range(atlist[i]):
            line = f.readline()
            m.append(line)
        mons.append(m)    

    comb = []
    monsN = range(len(atlist))
    for i in range(1,len(atlist) + 1):
        comb.append(list(it.combinations(monsN,i)))

    if not use_cp:
        for i in range(len(atlist)):
            fname = str(i + 1) + "b.xyz"
            ff = open(fname,'w')
            for j in range(len(comb[i])):
                inat = 0
                w=" "
                for k in range(len(comb[i][j])):
                    inat += atlist[comb[i][j][k]]
                    w += " " + str(comb[i][j][k] + 1)
                ff.write(str(inat) + "\n")
                ff.write(w + "\n")
                for k in range(len(comb[i][j])):
                    for l in mons[comb[i][j][k]]:
                        ff.write(l)
            ff.close()
    else:
        for i in range(len(atlist)):
            # Counterpoise
            fname = str(i + 1) + "b.xyz"
            ff = open(fname,'w')
            for j in range(len(comb[i])):
                w=" "
                for k in range(len(comb[i][j])):
                    w += " " + str(comb[i][j][k] + 1)
                ff.write(str(nat) + "\n")
                ff.write(w + "\n")
                for k in range(len(atlist)):
                    if  not k in comb[i][j]:
                        for l in mons[k]:
                            line = l.strip().split()
                            line[0] = line[0] + "1"
                            for mm in range(len(line)):
                                ff.write(line[mm] + " ")
                            ff.write("\n")
                for k in range(len(comb[i][j])):
                    for l in mons[comb[i][j][k]]:
                        ff.write(l)
            ff.close()
    return comb


# In[ ]:

def write_xyz(xyz,atlist,chglist,comb):
    f = open(xyz,'r')

    nat = f.readline().split()[0]
    f.readline()
    mons = []
    for i in range(len(atlist)):
        m = []
        for j in range(atlist[i]):
            line = f.readline()
            m.append(line)
        mons.append(m)    

    monsN = range(len(atlist))
    
    for i in range(len(atlist)):
        fname = str(i + 1) + "b.xyz"
        ff = open(fname,'r')
        foldname = str(i + 1) + "b"
        os.mkdir(foldname)
        for j in range(len(comb[i])):
            os.mkdir(foldname + "/" + str(j + 1))
            inat = int(ff.readline().split()[0])
            mns = ff.readline()
            fx = open(foldname + "/" + str(j + 1) + "/input.xyz", 'w')
            fx.write(str(inat) + "\n")
            fx.write(mns)
            for k in range(inat):
                fx.write(ff.readline())
            fx.close()
            fx = open(foldname + "/" + str(j + 1) + "/input.charge", 'w')
            c = 0
            for k in range(len(comb[i][j])):
                c += chglist[comb[i][j][k]]
            fx.write(str(c) + '\n')
            fx.close()
        ff.close()


# In[ ]:

# Obtain the different configurations
if mode == 1:
    comb = write_combs(fxyz, False, atlist)
    write_xyz(fxyz,atlist,chglist,comb)
elif mode == 2:
    comb = write_combs(fxyz, True, atlist)
    write_xyz(fxyz,atlist,chglist,comb)
elif mode == 3:
    comb = write_combs(fxyz, False, atlist)
    write_xyz(fxyz,atlist,chglist,comb)
    for i in range(len(atlist)):
        foldname = str(i + 1) + "b"
        for j in range(len(comb[i])):
            fi = foldname + "/" + str(j + 1)
            os.chdir(fi)
            atl = []
            chgl = []
            for k in range(len(comb[i][j])):
                atl.append(atlist[comb[i][j][k]])
                chgl.append(chglist[comb[i][j][k]])
            
                
            cmb = write_combs("input.xyz",True,atl)
            write_xyz("input.xyz",atl,chgl,cmb)
            os.chdir("../../")

else:
    print("Mode " + str(mode) + " not defined")
    sys.exit(1)


# In[ ]:

if mode == 1:
    print("\nYou run the XYZ preparation for non-counterpoise correction\n")
elif mode == 2:
    print("\nYou run the XYZ preparation with non-counterpoise correction for the whole cluster\n")
elif mode == 3:
    print("\nYou run the XYZ preparation with non-counterpoise correction for individual clusters\n")
    
if mode == 1 or mode == 2:
    a = """
Now you have all the XYZ in the 1b/1, 1b/2 ... , 2b... folders
Please, generate appropiate inputs run the calculations and save 
the TOTAL ENERGY in the file input.energy inside each folder.

Then run the second part of the script.
"""
elif mode == 3:
    a = """
Now you have all the XYZ in the 1b/1, 1b/2 ... , 2b... folders
Please, generate appropiate inputs run the calculations and save 
the TOTAL ENERGY in the file input.energy inside each folder.

Inside each one of the folders, there is a new tree that contains 
the coordinates with individual cluster counterpoise correction.
Please, generate appropiate inputs run the calculations and save 
the TOTAL ENERGY in the file input.energy inside each folder.

Then run the second part of the script.
"""
print(a)


# In[ ]:



