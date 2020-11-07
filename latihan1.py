#File ini digunakan untuk Tugas Latihan 1 pada materi Praktikum 3

print("Masukkan Nilai N : ")
n=int(input())

import random

for x in list(range(1,n+1,1)):
    print("Data ke: ",x,"=>",random.uniform(0,0.5))