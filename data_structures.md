# Data Structures ( Struktur data)


## method pada list
```
list.append(x)                     -> menambahkan item di akhir list

list.extend(iterable)              -> menambahkan semua item dari iterable

list.insert(i,x)                   -> menambahkan item berdasarkan posisi, i = index/posisi, x = item/nilai

list.remove(x)                     -> menghapus item pada list

list.pop([i])                      -> menghapus item berdasarkan index

list.clear()                       -> menghapus semua item di dalam list

list.index(x[,start[,end]])        -> menapilkan item berdasarkan index

list.count(x)                      -> menghitung berapa banyak item di dalam list

list.sort(key=None,reverse=False)  -> mengurutkan item di dalam list

list.reverse()                     -> membalikan urutan di dalam list

list.copy()                        -> menampilkan semua nilai list

````

# Mengunakan List sebagai Stacks
Stacks adalah struktur data di mana "last-in, last-out"
* Gunakan `list.append(item)` untuk menabah item di tumpukan atas
* Gunakan `list.pop()` untuk mengambil/mengeluarkan item di tumpukan atas

# Mengunakan List sebagai Queues
Queues adalah struktur data di mana "first-in, first-out"
* Gunakan standar library `collections.deque` 
* Gunakan `queue.append(item)` untuk menambah antrian terakhir
* Gunakan `queue.popleft()` untuk mengeluarkan item pada urutan pertama 

# List comprehensions
adalah **cara singkat untuk membuat list**
```
list = [item for item in sequence[,iterabel]]
        Or
list = [item for item in squence[,iterable] [if item expression]]
```

# Nested (bersarang) List comprehinsions
```
list = [ [item2 for in squence[,iterabel] ] for item in squence[,iterabel]]
``` 

# Tuples and Sequences
sama seperti list adalah sebuah **Sequence Types**, bedanya dengan list, tupel bersifat immutable, jadi nilai yang ada di dalamnya tidak bisa di rubah
```
tupel = nilai1,nilai2,nilai3,.. ,nilaike(n)
        atau
tupel = (nilai1,nilai2,nilai3,.. ,nilaike(n))
```

# Set ( himpunan)
python suppor tipe data yang sama dengan himpuanan matematika dan himpunan ini juga support operasi **union**, **intersection**, **difference**, **symmeteric difference**
```
set = {item1,item2,item3,.. ,item(n)}
        atau
set = set(iterable[,list,string]) 
```

# Dictionaries
tipe data ini termasuk golongan **Mapping Types**, kalau di bahasa pemrograman lain bisa di bilang "associative arrays" 
* index/key berupa immutable type
* tidak terurut

```
dict = {key:value, key2:value2,.. ,key-n:value-n}

# menabah key dan value di dictionary
dict[key_baru] = value_baru

# menghapus key dan value
del dict[key]

# meng-urutkan dictionary
sort(dict.keys())

# membuat dictionary dari sequence
dict(sequence)
```

# Teknik Perulangan

```
# mengunakan method items()
dictionary = {'oky':90, 'aggi':50, 'edy':10}
for key, value in dictionary.items():
        print(key,value)


# mengunakan fungsi enumerate()
for index, value in enumerate(sequence[,list]):
        print(index,value)


# perulangan 2 atau lebih sequence, dengan fungsi zip()
nama = ['oky','edy','aggi']
umur = [25,22,20]
for n,u in zip(nama,umur):
        print(nama, umur)

# perulangan mengunakan fungsi reversed()
for item in reversed(iterable[,list]):
        print(id)


# perulangan mengunakan fungsi sorted()
for sorted_item in sorted(set(basket)):
        print(sorted_item)


```
