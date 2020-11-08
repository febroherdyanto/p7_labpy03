# Tugas Pertemuan 7 - Praktikum 3 - p7_labpy03
Repository ini dibuat untuk memenuhi Tugas Bahasa Pemrograman - Pertemuan 7 - Praktikum 3
<hr>

Nama : Febro Herdyanto<br>
NIM : 312010043<br>
Kelas : TI.20.B.1<br>
<hr>

## Daftar Isi
| No | Description | Hyperlink |
| --- | --- | --- |
| 1 | Tugas Latihan 1 | [Click Here](#tugas-latihan-1) |
| 2 | Tugas Latihan 2 | [Click Here](#tugas-latihan-2) |
| 3 | Tugas Program 1 | [Click Here](#tugas-program-1) |

<hr>

Pada pertemuan 7 ini saya diberi tugas oleh Dosen untuk mempelajari dan membuat program sederhana dengan Bahasa Pemrograman Python<br>


## Tugas Latihan 1

* Pada tugas kali ini saya diminta dosen untuk mengerjakan tugas **latihan1.py**, seperti gambar dibawah ini :<br>
![Soal Latihan 1](pict/latihan1_soal.PNG)<br>

* Saya membuat source code dari perintah diatas (sesuai gambar), seperti dibawah ini :<br>
``` python
n=int(input("Masukkan Nilai N : "))

import random

for x in list(range(1, n+1, 1)):
    print(f"Data ke: {x} ->",random.uniform(0, 0.5))
``` 

Dari source code diatas akan saya jelaskan beberapa syntax atau function nya<br>
* Pada source code pertama, yaitu :<br>
``` python
import random
```
berfungsi untuk memasukkan *function random* yang ada didalam bahasa pemrograman python ke program yang telah saya buat.

* Untuk langkah kedua, penjelasan dari source code berikut :<br>
``` python
for x in list(range(1, n+1, 1)):
    print(f"Data ke: {x} ->",random.uniform(0, 0.5))
``` 

Fungsi **for** disini sebagai bentuk perulangan, selain menggunakan **for** kita juga bisa menggunakan function *while*. Untuk kali ini saya menggunakan fungsi **for** pada program.<br>
Penggunaan syntax default for adalah :<br>
> for index in range(jumlahperulangan):
>     perintah_yang_diulang








## Tugas Latihan 2


## Tugas Program 1
