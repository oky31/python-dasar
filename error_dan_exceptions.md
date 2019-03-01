# Errors dan Exceptions

* Raising Exception
* AssertionError Exception
* Blok try dan except
* Klause else dan finally

ada 2 jenis pesan kesalahan yaitu : **syntax errors** dan **exceptions**
- syntax errors -> kesalahan yang muncul karena secara syntax salah
- execptions -> kesalahan yang terjadi bukan karena syntax salah ......

## Exceptions
2 jenis exception :
- Build-in exceptions
- User definition  exceptions

## Assertion
ini adalah salah satu teknik untuk memunculkan exception berdasarkan expressi dari sebuah statment. jadi expressi harus bernilai benar, jika bernilai salah akan mucul `AssertionError`

```
assert Expression[, Arguments]
```

Contoh  Pengunaan   
```
def check_integer(number):
    assert not int(number), "harus Integer"
```
jika kode di atas menerima parameter selain integer akan muncul AssertionError
```
>> check_integer(2.123)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in check_integer
AssertionError: harus Integer

```


