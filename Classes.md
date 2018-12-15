# Classes
- Class di dalam python menyediakan semua fitur standar  Object Orientid Progamming
- Mengizinkan Multiple Base class
- class turunan bisa override setiap method  pada base class
- Object bisa berisi data yang banyak
- class bersifat dinamis, artinya  bisa di modifikasi setelah di buat
- normalnya setial anggota class adalah public dan semua fungsi adalah virtual
- setiap method di dalam object wajib di deklarasikan dengan 1 argument yang me-representasikan sebuah object

# Python Scopes dan Namespace
Namespace adalah pemetaan untuk penamaan sebuah object, dan di implentasikan menunakan python dictionaries

# python prinsip
Assignment do not copy data, they just bind names to objects

# Mendefinisikan class
```
class namaClass:
    <statement-1>
    .
    .
    <statement-n>
```

# Class Objects
Object dari class mendukung 2 jenis operasi yaitu :
- attribute references -> `object.namaAttribut`
- instantiation (nstantsiasi) -> `variabel = namaClass()`

ketika sebuah class yang mendefinisikan method `__init__()` , maka setiap argumen yang ada di dalam method `__init__()` harus di ikutsertakan ketika men-instansiasi object tersebut

# Instance Objects
ada 2 jenis attribut references yaitu :   
- data attributes
- method

# method objects
```
object.namaMethod()
```

# class dan Instance Variabel
- setiap object dari 1 kelas yang sama, memiliki nilai attribut dan method yang unik
- share nilai attribut atau method memungkinkan di lakukan dengan mengunakan **mutable objects** seperti list dan dictionaries. 

# Random Remarks
- class tidak benar-benar meng-implemntasi tipe data abstract
- di dalam python tidak ada yang memungkinkan untuk memaksakan penyembunyian data (data hiding)
- 


# saran
- Gunakan verbs untuk penamaan methods
- Gunakan nouns untuk penamaan data attributes

# Inheritance
```
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    <statement-N>
```

# Multiple Inheritance
```
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

# Private Variabels
```
__namaVariabel
```

# Iterators
```
__iter__()
__next__()
```


# Generators
Adalah Alat untuk membuat Iterator . ketika mereturnkan data gunakan statment `yield` 