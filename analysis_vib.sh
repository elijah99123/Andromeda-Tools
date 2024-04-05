#!/usr/bin/env bash 
#run from main dir
#add Get_disp.py, mesh.conf to main
#add remove_forces to main with atom indicies


set python = "/data/beginel/.conda/envs/phonopy/bin/python"
set phonopy = "/data/beginel/.conda/envs/phonopy/bin/phonopy"


mkdir start/other
mkdir TS/other
mkdir end/other

cp -f ./start/POSCAR ./start/other/POSCAR
cp -f ./Get_disp.py ./start/other/

cp -f ./TS/POSCAR ./TS/other/POSCAR
cp -f ./Get_disp.py ./TS/other/

cp -f ./end/POSCAR ./end/other/POSCAR
cp -f ./Get_disp.py ./end/other/

cd ./start/other
python Get_disp.py
mv -f POSCAR POSCAR_old
mv -f CONTCAR POSCAR
phonopy -d --dim="1 1 1"

cd ../../TS/other
python Get_disp.py
mv -f POSCAR POSCAR_old
mv -f CONTCAR POSCAR
phonopy -d --dim="1 1 1"

cd ../../end/other
python Get_disp.py
mv -f POSCAR POSCAR_old
mv -f CONTCAR POSCAR
phonopy -d --dim="1 1 1"
cd ../../

mkdir ./start/Needed/Completed/Yang
mkdir ./TS/Needed/Completed/Yang
mkdir ./end/Needed/Completed/Yang

cp -f ./start/other/phonopy_disp.yaml ./start/Needed/Completed/Yang/
cp -f ./TS/other/phonopy_disp.yaml ./TS/Needed/Completed/Yang/
cp -f ./end/other/phonopy_disp.yaml ./end/Needed/Completed/Yang/
cp -f ./mesh.conf ./start/Needed/Completed/Yang/
cp -f ./mesh.conf ./TS/Needed/Completed/Yang/
cp -f ./mesh.conf ./end/Needed/Completed/Yang/

cd ./start/Needed/Completed/Yang/

for i in ../*/
do
 name="$(basename $i)"
 if [ ! $name == "Yang" ]
 then 
  num=$(echo $name | tr -dc 0-9)
  printf -v num1 "%04d" $num
  name1="POSCAR-"$num1
  mkdir ./$name1
  cp ../$name/vasprun.xml ./$name1/vasprun.xml
  cp ../../../../remove_forces.py ./$name1/
  cd ./$name1
  python remove_forces.py vasprun.xml new_vasprun.xml
  cd ..
 fi
done
phonopy -f */new_vasprun.xml
phonopy --dos --qpoints 0 0 0 --eigvecs
phonopy -t --mesh 12 12 12

cd ../../../../

cd ./TS/Needed/Completed/Yang/

for i in ../*/
do
 name="$(basename $i)"
 if [ ! $name == "Yang" ]
 then 
  num=$(echo $name | tr -dc 0-9)
  printf -v num1 "%04d" $num
  name1="POSCAR-"$num1
  mkdir ./$name1
  cp ../$name/vasprun.xml ./$name1/vasprun.xml
  cp ../../../../remove_forces.py ./$name1/
  cd ./$name1
  python remove_forces.py vasprun.xml new_vasprun.xml
  cd ..
 fi
done
phonopy -f */new_vasprun.xml
phonopy --dos --qpoints 0 0 0 --eigvecs
phonopy -t --mesh 12 12 12

cd ../../../../

cd ./end/Needed/Completed/Yang/

for i in ../*/
do
 name="$(basename $i)"
 if [ ! $name == "Yang" ]
 then 
  num=$(echo $name | tr -dc 0-9)
  printf -v num1 "%04d" $num
  name1="POSCAR-"$num1
  mkdir ./$name1
  cp ../$name/vasprun.xml ./$name1/vasprun.xml
  cp ../../../../remove_forces.py ./$name1/
  cd ./$name1
  python remove_forces.py vasprun.xml new_vasprun.xml
  cd ..
 fi
done
phonopy -f */new_vasprun.xml
phonopy --dos --qpoints 0 0 0 --eigvecs
phonopy -t --mesh 12 12 12

cd ../../../../
echo "done"
