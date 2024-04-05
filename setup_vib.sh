#!/usr/bin/env bash 

#run check_disp and setup a_vibration_pick
#need INCAR POTCAR good_sub KPOINTS ArunVib_2 

module load anaconda
conda activate phonopy

mkdir start
mkdir TS
mkdir end

sleep 1

cp POSCAR start/POSCAR
cp mid.vasp TS/POSCAR
cp CONTCAR end/POSCAR

sleep 1

cd start
phonopy -d --dim="1 1 1"

cd ../TS 
phonopy -d --dim="1 1 1"

cd ../end
phonopy -d --dim="1 1 1"
cd ..

cp ./avibration-pick.py ./start/
cp ./avibration-pick.py ./TS/
cp ./avibration-pick.py ./end/

sleep 1

cd start
python avibration-pick.py

cd ../TS 
python avibration-pick.py

cd ../end
python avibration-pick.py
cd ..

mkdir ./start/Needed/Completed
mkdir ./TS/Needed/Completed
mkdir ./end/Needed/Completed

sleep 1

cp ./ArunVib_2.sh ./start/Needed/Completed/
cp ./ArunVib_2.sh ./TS/Needed/Completed/
cp ./ArunVib_2.sh ./end/Needed/Completed/
cp ./INCAR ./start/Needed/Completed/
cp ./INCAR ./TS/Needed/Completed/
cp ./INCAR ./end/Needed/Completed/
cp ./KPOINTS ./start/Needed/Completed/
cp ./KPOINTS ./TS/Needed/Completed/
cp ./KPOINTS ./end/Needed/Completed/
cp ./good_sub.py ./start/Needed/Completed/
cp ./good_sub.py ./TS/Needed/Completed/
cp ./good_sub.py ./end/Needed/Completed/
cp ./POTCAR ./start/Needed/Completed/
cp ./POTCAR ./TS/Needed/Completed/
cp ./POTCAR ./end/Needed/Completed/

sleep 1

cd ./start/Needed/Completed
chmod +x ArunVib_2.sh
./ArunVib_2.sh

cd ../../../TS/Needed/Completed
chmod +x ArunVib_2.sh
./ArunVib_2.sh

cd ../../../end/Needed/Completed
chmod +x ArunVib_2.sh
./ArunVib_2.sh


