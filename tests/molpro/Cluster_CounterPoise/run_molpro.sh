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
for i2 in `ls -d ?b`; do 
  cd $WD/$i2 
  for j2 in `ls -d *`; do
    cd $WD/$i2/$j2
    for i in `ls -d ?b`; do
      cd $WD/$i2/$j2/$i
      for j in `ls -d *`; do
        cd $WD/$i2/$j2/$i/$j
        nat=`head -n 1 input.xyz | awk '{print $1}'`
        tail -n $nat input.xyz > stdTMP
        chg=`head -n 1 input.charge | awk '{print $1}'`
        cat $WD/HEAD stdTMP $WD/TAIL | sed "s/XXXXXX/$chg/g" | sed "s/YYYYYY/0/g" > input
        molpro -n 1 -o input.log -d $HOME/MOLPRO_SCRATCH/ -W $HOME/MOLPRO_WFN input
        grep "SETTING FRAGMENT_ENERGY" input.log | awk '{print $3}' > input.energy
        rm input.xml stdTMP 
      done
    done
    echo "$i2/$j2 done"
  done
done

cd $WD 
rm HEAD TAIL
