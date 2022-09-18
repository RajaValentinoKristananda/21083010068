x=$(( 1*2 ))
y=$(( 1/2 ))

echo "x=$x"
echo "y=$y"

if [ $x == $y ]
then
echo "x sama dengan y"
elif [ $x -gt $y ]
then
echo "x lebih besar dari y"
elif [ $x -lt $y ]
then
echo "x lebih kecil dari y"
else
echo "Tidak ada kondisi yang memenuhi"
fi
