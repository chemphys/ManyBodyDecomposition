
# coding: utf-8

# In[15]:

import itertools as it
import sys
import os
import math


# In[16]:

if len(sys.argv) != 4:
    print("Usage: python3 " + sys.argv[0] + " N  mode monomer" )
    print("N is the max N-body contribution you want")
    print("monomer is the monomer name of the contributions you want to separate")
    print("If monomer == h2o , the contributions from fragments with only h2o will be separated from the rest")
    sys.exit(1)
nbmaxg = int(sys.argv[1])
mode = int(sys.argv[2])
monomer = sys.argv[3]
monnames = ["co2","co2","co2","co2","co2"]
atlistg = [3,3,3,3,3]
opt_mon_eng = [-185.06839054,-185.06839054,-185.06839054,-185.06839054,-185.06839054]
unit_convertion = 627.509;
#atlist = [3,3]
#opt_mon_en = [-186.561257471,-186.561257471]
#nbmaxg = 5

nb = len(atlistg)

# In[17]:

def get_mb(nbmax,atlist,opt_mon_en,my_monnames):
    # Getting data we will need
    nb = len(atlist)
    nm = []
    monsN = range(1,nb + 1)
    combs = []
    for i in range(1,nb+1):
        combs.append(list(it.combinations(monsN,i)))
        nm.append(len(combs[i-1]))
    # Store energies
    energies = []
    for i in range(nbmax):
        foldname = str(i + 1) + "b"
        nbEn = []
        for j in range(nm[i]):
            fold = foldname + "/" + str(j+1)
            ff = open(fold + "/input.energy", 'r')
            nbEn.append(float(ff.readline().split()[0]))
        energies.append(nbEn)
    # Get 1b
    enb = []
    e = []
    enb_A = []
    enb_B = []
    e_A = []
    e_B = []
    for i in range(nm[0]):
        my_e = energies[0][i] - opt_mon_en[i]
        e.append(my_e)
        if monnames[i] == monomer:
            e_A.append(my_e)
            e_B.append(0.0)
        else:
            e_B.append(my_e)
            e_A.append(0.0)

    enb.append(e)
    enb_A.append(e_A)
    enb_B.append(e_B)
    
    # Get the many-body contributions (>1B)
    # Loop overall the nb contributions
    for nbx in range(1,nbmax):
        n = nbx + 1
        # Get the nbx-yh body contribution for each fragment
        e = []
        e_A = []
        e_B = []
#        print("NBX = " + str(nbx))
#        print(combs[nbx])
        for frag in combs[nbx]:
            sumE = []
            e.append(0.0)
            e_A.append(0.0)
            e_B.append(0.0)
            x = len(e) - 1
            # Loop over all the nth subfragments of the cluster
            for k in range(1,len(frag) + 1):
                sumE.append(0.0)
                icomb = list(it.combinations(frag,k))
                for l2 in range(len(icomb)):
                    for l in range(1,len(combs[k - 1]) + 1):
                        filename = str(k) + "b/" + str(l) + "/input.xyz"
                        ff = open(filename)
                        ff.readline()
                        refcomb = ff.readline().split()
                        ff.close()
                        refcomb = [int(i) for i in refcomb]
                        if sorted(refcomb) == sorted(list(icomb[l2])):
                            sumE[k-1] += energies[k-1][l-1]
                            break
            Nmax = len(frag)
            for m2 in range(n):
                m = m2 + 1
                one = pow(-1,Nmax - m )
                a = math.factorial(Nmax - m )
                b = math.factorial(k - m)
                c = math.factorial(Nmax - k)
                g = one * a / b / c
                my_e = g * sumE[m2]
                e[x] += my_e

            # check if monomer is in fragment
            is_A = True
            for mon_id in range(len(frag)):
                my_id = int(frag[mon_id])
#                print(monomer + " vs " + monnames[my_id - 1])
#                print(frag)
                if monomer != my_monnames[my_id - 1]:
                    is_A = False
                    break

            if is_A:
                e_A[x] += e[x]
            else:
                e_B[x] += e[x]

        enb.append(e)
        enb_A.append(e_A)
        enb_B.append(e_B)
    return enb, enb_A, enb_B


# In[ ]:




# In[ ]:


        


# In[18]:

if mode == 1 or mode == 2:

    enb, enb_A, enb_B = get_mb(nbmaxg,atlistg,opt_mon_eng,monnames)

    # Printing results
    be = 0.0
    for i in range(len(enb)):
        enb[i] = [k * unit_convertion for k in enb[i]]
        be += sum(enb[i])
        print(str(i+1) + "b = " + str(sum(enb[i])))
    if nbmaxg == nb:
        print("Interaction Energy = " + str(be - sum(enb[0])))
        print("Binding Energy     = " + str(be))
    for i in range(len(enb)):
        print(" ")
        print("Individual " + str(i+1) + "-body contributions:")
        for j in range(len(enb[i])):
            print("Fragment " + str(j+1) + ": " + str(enb[i][j]) )

    # Print individual contributions
    print("\nContributions by monomer:")
    
    print("NB  =    [with only " + monomer + "]      [other a part from " + monomer + "]     Total")
    for i in range(len(enb)):
        enb_A[i] = [k * unit_convertion for k in enb_A[i]]
        enb_B[i] = [k * unit_convertion for k in enb_B[i]]

        print(str(i+1) + "b  = " + str(sum(enb_A[i])) + "     " + str(sum(enb_B[i])) + "     "  + str(sum(enb[i]))) 
        

elif mode == 3:
    nb = len(atlistg)
    nm = []
    monsN = range(1,nb + 1)
    comb = []
    enb = []
    enb_A = []
    enb_B = []
    for i in range(1,nb+1):
        comb.append(list(it.combinations(monsN,i)))
        nm.append(len(comb[i-1]))
    for i in range(nbmaxg):
        enb.append([])
        enb_A.append([])
        enb_B.append([])
        foldname = str(i + 1) + "b"
        for j in range(len(comb[i])):
            atl = []
            monen = []
            monnamesl = []
            for k in range(len(comb[i][j])):
                atl.append(atlistg[comb[i][j][k] -1])
                monen.append(opt_mon_eng[comb[i][j][k]-1])
                monnamesl.append(monnames[comb[i][j][k]-1])
            os.chdir(foldname + "/" + str(j+1))
            enbx, enb_xa, enb_xb = get_mb(i+1,atl,monen,monnamesl)
            enb[i].append(enbx[i][0])
            enb_A[i].append(enb_xa[i][0])
            enb_B[i].append(enb_xb[i][0])
            os.chdir("../../")
            
    # Printing results
    be = 0.0
    for i in range(len(enb)):
        enb[i] = [k * unit_convertion for k in enb[i]]
        be += sum(enb[i])
        print(str(i+1) + "b = " + str(sum(enb[i])))
    if nbmaxg == nb:
        print("Interaction Energy = " + str(be - sum(enb[0])))
        print("Binding Energy     = " + str(be))
    for i in range(len(enb)):
        print(" ")
        print("Individual " + str(i+1) + "-body contributions:")
        for j in range(len(enb[i])):
            print("Fragment " + str(j+1) + ": " + str(enb[i][j]) )

    # Print individual contributions
    print("\nContributions by monomer:")

    print("NB  =    [with only " + monomer + "]      [other a part from " + monomer + "]     Total")
    for i in range(len(enb)):
        enb_A[i] = [k * unit_convertion for k in enb_A[i]]
        enb_B[i] = [k * unit_convertion for k in enb_B[i]]
       
        print(str(i+1) + "b  = " + str(sum(enb_A[i])) + "     " + str(sum(enb_B[i])) + "     "  + str(sum(enb[i])))

