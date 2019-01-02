def tebak_harga(harga):
    if harga < 0 :
        raise Exception('Harga Tidak boleh kurang dari 0 !')
    
    if harga == 5000:
        return 'benar !'
    else :
        return 'salah !'

harga = int(input('harga : '))
hasil = tebak_harga(harga)
print(hasil)