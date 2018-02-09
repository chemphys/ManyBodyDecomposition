#!/bin/bash

# 1. Get MB decomp xyzs
python3 ../../../src/1-get_mb_xyz.py cluster.xyz 2

# 2. Run calculations
chmod 755 run_molpro.sh
./run_molpro.sh
chmod 644 run_molpro.sh

# 3. Get many-body energies
python3 ../../../src/3-get_mb_decomp.py 5 2
