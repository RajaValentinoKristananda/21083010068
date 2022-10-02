echo "Masukkan Angka Pertama"
read angka1
echo "Masukkan Angka Kedua"
read angka2

select Menu in + - cukup
do
   case $Menu in
      +)
         hasil=$((angka1 + angka2))
         echo $hasil
      ;;
      -)
         hasil=$((angka1 - angka2))
         echo $hasil
      ;;
      cukup)
         break
      ;;
   esac
done
