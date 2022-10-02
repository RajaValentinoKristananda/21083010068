echo "Masukkan Angka Positif :"
read angka

until [ ! $angka -gt 0 ]
do
   echo $angka
   angka=$((angka-2))
done

