# Control flow

## if Statements



## for statements
statement **for** di python berbeda dari bahasa pemrograman yang lain, di dalam C dan pascal statment **for** selalu meng-iterasi atau mengulangi deret aritmatik. tetapi di 
python **for** meng-iterasi item dari sequence yang sudah ada (list,string)

```
    for item in list:
        expression
```

## fungsi range()
jika membutuhkan iterasi untuk angka yang berurut maka gunakan built-in function `range()`

* range() bukanlah object yang menghasilkan list, tapi berprilaku seolah2 list
* range() hanya object yang mengembalikan nilai berurut, dari urutan yang di inginkan

## break, continue statements, dan else pada loops
* `break` -> untuk menghentikan dari perulangan `for` atau `while`
* `else`  -> else bisa di letakan di `for` atau `while` dan expresi yang ada di dalam else di jalankan ketika perulangan `dihentikan(terminate)` atau bernilai `false`
* `continue` -> 

## `pass` Statement
`pass` statement tidak melakukan apa-apa, sebuah objek yang mengunakan statement ini tidak akan melakukan apa2.


## Mendefinisikan Fungsi
untuk mendefinisikan fungsi gunakan keyworad `def`
```
def nama_fungsi(parameter):
    expressi
```

* di dalam fungsi tidak bisa memangil variabel global
* nilai default pada parameter fungsi hanya di evaluasi 1 kali. ini berarti pada objek yang bersifat mutable seperti list,dictionary nilai default yang sudah di manipuasi akan sama dengan nilai default untuk deklasri fungsi selanjutnya

**fungsi dengan default value**
```
def nama_fungsi(parameter = nilai):
    expressi
```

**Arbitary Argument List ( jumlah argumen yang suka-suka)**
```
def nama_fungsi(*parameter):
    expressi
```

## Lambda Expressions
untuk mendefiniskan fungsi tanpa nama gunakan keyword  `lambda` keyworad ini akan mengemblikan sebuah nilai

```
lambda [list_parameter] : expresi
```

## Dokumentasi Fungsi
**Aturan**
* baris pertama harus singkat, terdiri dari tujuan akhir fungsi, dan diawali dengan huruf besar dan di akhiri dengan tanda titik
* jika inggin menabhakan keterangn, beri ruang kosong 1 baris setelah baris pertama


