#!/bin/bash

cat << EOF > HEAD
memory,64,M

geomtyp=xyz
geometry={
EOF

cat << EOF > TAIL
}

basis={
default=STO-3g
}

CHARGE = XXXXXX, SPIN = YYYYYY
dummy,C1,O1
hf

FRAGMENT_ENERGY = ENERGY

EOF

WD=$PWD
for i in `ls -d ?b`; do 
  cd $WD/$i 
  for j in `ls -d *`; do
    cd $WD/$i/$j
    nat=`head -n 1 input.xyz | awk '{print $1}'`
    tail -n $nat input.xyz > stdTMP
    chg=`head -n 1 input.charge | awk '{print $1}'`
    cat $WD/HEAD stdTMP $WD/TAIL | sed "s/XXXXXX/$chg/g" | sed "s/YYYYYY/0/g" > input
    molpro -n 1 -o input.log -d $HOME/MOLPRO_SCRATCH_2/ -W $HOME/MOLPRO_WFN_2 input
    grep "SETTING FRAGMENT_ENERGY" input.log | awk '{print $3}' > input.energy
    rm input.xml stdTMP 
    echo "$i/$j done"
  done
done

cd $WD 
rm HEAD TAIL
