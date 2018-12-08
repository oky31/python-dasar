# Modules (Modul)
sekumpulan kode python yang  di muat di dalam file. modul bisa berisi executable satements atau fungsi

```
# import statement di dalam modul secara langsung
from nama_modul import fungsi[,class], fungsi2[,class2]

# import semua statement yang di definisikan di dalam modul ( tidak di sarankan)
form nama_modul import *

# alias (as) di dalam modul
from nama_modul as nama_baru
    atau
from nama_modul import fungsi[,class] as nama_baru


```

# Eksekusi Modul sebagai script
modul bisa di eksekusi sebagi script dengan menambahkan `__name__` dan `"__main__"` di dalam file modul
```
if __name__ == "__main__":
    import sys
    nama_fungsi(tipe_data(sys.argv[1]))
```

cara menjalankan script 
```
python nama_modul.py <arguments>
```

# Fungsi dir()
fungsi ini di gunakan untuk melihat ada statment dan fungsi apa saja yang ada di dalam modul
```
dir(nama_modul)
```

# Package
adalah sekumpulan modul. di bawah ini adalah struktur dari package

```
nama_package/
    __init__.py        #inisialiasi package
    sub_package/
        __init__.py
        modul_1.py
        modul_2.py
        ..
    sub_package2/
        __init__.py
        modul_3.py
        modul_4.py
        ...
    ...

```