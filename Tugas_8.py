from os import getpid
from time import time,sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
   if (i+1)%2==0:
      print(i+1, "genap - ID Process", getpid())
   else:
      print(i+1, "ganjil - ID Process", getpid())
   sleep(1)

n=int(input("Nilai angka batasan? "))
print("\n")

sekuensial_awal = time()
print("Sekuensial")
for i in range(n):
   cetak(i)
sekuensial_akhir=time()
print("\n")

process_awal=time()
print("Multiprocessing.process")
for i in range(n):
    p=Process(target=cetak, args=(i, ))
    p.start()
    p.join()
process_akhir=time()
print("\n")

pool_awal=time()
pool = Pool()
print("Multiprocessing.pool")
pool.map(cetak,range(0,n))
pool.close()
pool_akhir=time()
print("\n")

print("Hasil Perbandingan waktu")
print("Waktu eksekusi Sekuensial:", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi kelas Process:", process_akhir - process_awal, "detik")
print("Waktu eksekusi kelas Pool:", pool_akhir - pool_awal, "detik")
