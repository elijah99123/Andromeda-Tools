for i in {00..14}; do  cp ./simplify.py ./$i/;  cd ./$i;  python simplify.py;  cd ../; done