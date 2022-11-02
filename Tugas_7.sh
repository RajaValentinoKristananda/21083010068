panjang() {
   echo "Masukkan Panjang :"
   read panjang
}

lebar() {
   echo "Masukkan Lebar :"
   read lebar
}

luas() {
   echo "Program Menghitung Luas Bidang Persegi"
   panjang
   lebar
   let luas=$panjang*$lebar
   echo "Luas Persegi : $luas"
}

luas
