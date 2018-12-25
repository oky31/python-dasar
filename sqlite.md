# Python-SQLite
SQLite adalah DBMS yang sudah otomatis terinstal di python, jadi kita tidak perlu melakukan instalasi lagi cukup dengan mengunakan modul `SQLite3`

# Langkah Pengunaan
1. Buat Koneksi database 
```
koneksi = sqlite3.connect('nama_file.db')
```

2. Buat Cursor object
```
cursor = koneksi.cursor()
```
3. Eksekusi Statement sql
```
cursor.execute(''' Statement Sql ''')
```
4. Simpan Perubahan Dengan Commit()
```
koneksi.commit()
```
5. Tutup Koneksi
```
koneksi.close()
```


# Ini Masih Bersambung Di tunggu kelanjutanya ya .....