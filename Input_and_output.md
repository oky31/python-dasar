# Pemformatan String
Method untuk memformat String
```
- str.format()
- str.rjust()
- str.ljust()
- str.center()
- str.zfill()

```

### str.format()
method ini bisa mensubtitusikan nilai ke dalam sebuah string  
```
"kata1 {0} kata2{1} kata3{3}".format(variabel0,variabel1,variabel3)
        atau
"kata1 {variabel1} kata2{variabel2} kata3{variabel3}".format(variabel1,variabel2,variabel3)
```

# Memformat String dengan Gaya lama
mengunakan operator '%' di dalam string

# Membaca Dan Menulis File
`open(namafile, mode)` fungsi yang di gunakan untuk membaca sebuah file dengan mode sebagai berikut :
```
r -> hanya membaca file
w -> hanya menulis isi file
a -> untuk menambahkan isi file
r+ -> untuk membaca dan menulis file
b  -> untuk membuka file dalam mode biner
```

## prakte yang baik guankan `with`
```
with open(namafile) as nama_alias:
    variabel_penampung = nama_alias.read()
```
file yang di buka dengan with harus di tutup dengan statment
```
nama_alias.closed
```

## method yang di gunakan setelah file di panggil
```
file.read() ->
file.readline() ->
file.write(string_yang_akan_ditambah) ->
```