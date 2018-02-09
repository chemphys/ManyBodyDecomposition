# ManyBodyDecomposition
A set of scripts to obtain many body decomposition energies. 
Keywords: Computational Chemistry, Theoretical Chemistry, Many Body Interactions, Electronic Structure

## Many Body Decomposition Background
The total binding energy of an N-molecule system can be decomposed in contributions of one-body (1B), two-body (2B), ... , N-body (NB). In [this paper](http://aip.scitation.org/doi/abs/10.1063/1.4742816) they present, in Equation 7, a recursive formula used to calculate the many body interactions. This expression is the one used in this package.

## Installation and Usage
This package does not require installation. However, it will require python3 to work. 

In order to get the Many-Body decomposition, follow the following steps:

1. Open with a text editor the file `1-get_mb_xyz.py`, and modify the two lines:
```
atlist = [3,3,3,3,3]
chglist = [0,0,0,0,0]
```
   In these lines, atlist contains a python list of the number of atoms in each fragment. As an example, if you have a cluster with 5 CO2 molecules, you will put `atlist = [3,3,3,3,3]`, since each CO2 has 3 atoms. If you have 1 Na ion, 3 H2O molecules and one Cl anion, you will put `atlist = [1,3,3,3,1]`
   The `chglist` list contains the charge of each individual fragment. For the 5 CO2 molecule cluster, this will be `chglist = [0,0,0,0,0]`, since all the CO2 are neutral. For the Na+, 3H2O, Cl-, you will put `chglist = [1,0,0,0,-1]`.

2. Run the python script `1-get_mb_xyz.py` as:
```
python3 1-get_mb_xyz.py CLUSTER.xyz MODE
```
The first argument, `CLUSTER.xyz`, is a file containing the coordinates of your whole system in the XYZ format.
The second argument, `MODE`, is an integer with values 1, 2 or 3.
* Mode 1. No counterpoise correction. The fragments will be written as they are, with no ficticious atoms.
* Mode 2. Full cluster counterpoise correction. The fragments will be written as real atoms, and the rest of the atoms of the cluster that do not belong to that fragment will be tagged with a `1` after the atom name. Since different electronic structure codes treat the ghost atoms in a different way, that will be up to the user on how to tell the code that they need to be dummy atoms.
* Mode 3. Cluster counterpoise correction. The n-body contribution of each fragment will be obtained by performing counterpoise correction ONLY in that cluster.

After the script is run, you will get a tree with the folders 1b, 2b, ..
This is an example of a tree for a 5 CO2 molecule cluster:
```
.
├── 1b
│   ├── 1
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 2
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 3
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 4
│   │   ├── input.charge
│   │   └── input.xyz
│   └── 5
│       ├── input.charge
│       └── input.xyz
├── 1b.xyz
├── 2b
│   ├── 1
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 10
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 2
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 3
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 4
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 5
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 6
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 7
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 8
│   │   ├── input.charge
│   │   └── input.xyz
│   └── 9
│       ├── input.charge
│       └── input.xyz
├── 2b.xyz
├── 3b
│   ├── 1
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 10
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 2
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 3
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 4
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 5
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 6
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 7
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 8
│   │   ├── input.charge
│   │   └── input.xyz
│   └── 9
│       ├── input.charge
│       └── input.xyz
├── 3b.xyz
├── 4b
│   ├── 1
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 2
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 3
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 4
│   │   ├── input.charge
│   │   └── input.xyz
│   └── 5
│       ├── input.charge
│       └── input.xyz
├── 4b.xyz
├── 5b
│   └── 1
│       ├── input.charge
│       └── input.xyz
├── 5b.xyz
├── cluster.xyz
```

The 1b.xyz, 2b.xyz ... files are all the monomers, dimers... and so on.
Inside each nb folder, there are several folders, numbered, that contain the input.xyz for that fragment, and the input.charge with the charge of the fragment. This last file will be useful when generating the quantum chemistry input files.

This tree is only valid for modes 1 and 2. For mode 3, the tree is slightly more complicated. Inside each `nb/K/` folder, there will be a new tree like in modes 1 and 2, but ONLY for that concrete fragment. This allows to perform the cluster counterpoise correction. This is an example of the directory tree using mode 3.
```
.
├── 1b
│   ├── 1
│   │   ├── 1b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 2
│   │   ├── 1b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 3
│   │   ├── 1b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 4
│   │   ├── 1b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   └── 5
│       ├── 1b
│       │   └── 1
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 1b.xyz
│       ├── input.charge
│       └── input.xyz
├── 1b.xyz
├── 2b
│   ├── 1
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 2
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 10
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 2
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 2
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 2
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 3
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 2
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 4
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 2
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 5
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 2
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 6
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 2
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 7
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 2
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 8
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 2
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   └── 9
│       ├── 1b
│       │   ├── 1
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   └── 2
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 1b.xyz
│       ├── 2b
│       │   └── 1
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 2b.xyz
│       ├── input.charge
│       └── input.xyz
├── 2b.xyz
├── 3b
│   ├── 1
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 10
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 2
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 3
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 4
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 5
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 6
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 7
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 8
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 3
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   └── 9
│       ├── 1b
│       │   ├── 1
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 2
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   └── 3
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 1b.xyz
│       ├── 2b
│       │   ├── 1
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 2
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   └── 3
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 2b.xyz
│       ├── 3b
│       │   └── 1
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 3b.xyz
│       ├── input.charge
│       └── input.xyz
├── 3b.xyz
├── 4b
│   ├── 1
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 4
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 4
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 5
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 6
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 4
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── 4b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 4b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 2
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 4
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 4
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 5
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 6
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 4
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── 4b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 4b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 3
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 4
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 4
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 5
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 6
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 4
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── 4b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 4b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   ├── 4
│   │   ├── 1b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 4
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 1b.xyz
│   │   ├── 2b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 4
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 5
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 6
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 2b.xyz
│   │   ├── 3b
│   │   │   ├── 1
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 2
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   ├── 3
│   │   │   │   ├── input.charge
│   │   │   │   └── input.xyz
│   │   │   └── 4
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 3b.xyz
│   │   ├── 4b
│   │   │   └── 1
│   │   │       ├── input.charge
│   │   │       └── input.xyz
│   │   ├── 4b.xyz
│   │   ├── input.charge
│   │   └── input.xyz
│   └── 5
│       ├── 1b
│       │   ├── 1
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 2
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 3
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   └── 4
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 1b.xyz
│       ├── 2b
│       │   ├── 1
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 2
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 3
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 4
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 5
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   └── 6
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 2b.xyz
│       ├── 3b
│       │   ├── 1
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 2
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 3
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   └── 4
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 3b.xyz
│       ├── 4b
│       │   └── 1
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 4b.xyz
│       ├── input.charge
│       └── input.xyz
├── 4b.xyz
├── 5b
│   └── 1
│       ├── 1b
│       │   ├── 1
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 2
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 3
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 4
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   └── 5
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 1b.xyz
│       ├── 2b
│       │   ├── 1
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 10
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 2
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 3
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 4
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 5
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 6
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 7
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 8
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   └── 9
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 2b.xyz
│       ├── 3b
│       │   ├── 1
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 10
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 2
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 3
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 4
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 5
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 6
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 7
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 8
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   └── 9
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 3b.xyz
│       ├── 4b
│       │   ├── 1
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 2
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 3
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   ├── 4
│       │   │   ├── input.charge
│       │   │   └── input.xyz
│       │   └── 5
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 4b.xyz
│       ├── 5b
│       │   └── 1
│       │       ├── input.charge
│       │       └── input.xyz
│       ├── 5b.xyz
│       ├── input.charge
│       └── input.xyz
├── 5b.xyz
```

3. Obtain the energies of each input.xyz file, and save the total energy (binding energy if using forcefields, and total energy if using a quantum chemistry package) IN HARTREES in a file called `input.energy`. The name MUST be this one.

4. Open the `3-get_mb_decomp.py` file, and modify the lines:
```
atlistg = [3,3,3,3,3]
opt_mon_eng = [-185.06839054,-185.06839054,-185.06839054,-185.06839054,-185.06839054]
```
  The list `atlistg` is the same as in the first script. The second list, `opt_mon_eng`, is the energy of the optimized monomers, in the same order as in the `atlistg`. That energy MUST be in HARTREES.

5. Finally, run the python script `3-get_mb_decomp.py` as:
```
python3 3-get_mb_decomp.py N MODE
```
`MODE` is the same as it was for the first script, and `N` is the maximum nb contribution you want to get. Usually is set to the number of molecules, but maybe you just want the lowest n-body contributions. That depends.
This script will print a full many body decomposition, with the contribution of each N-body fragment to the N-body energy.

## Notes
* You can have a look at the test folder to see an example of usage for each mode for a (CO2)5 cluster.
* Please, report any problem you have and I will be happy to help.
