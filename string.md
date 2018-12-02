# String 
Setiap string didalam python di nyatakan dalam  tanda yaitu
	
	'...' -> tanda kutip tunggal
	"..." -> tanda kutip ganda 
	'''...''' -> tanda kutip tunggal triple
	"""...""" -> tanda kutip double triple


untuk membuat string mudah di baca gunakan fungsi **print()**, fungsi ini \n
di gunakan untuk mencetak expresi ke layar.

## Contoh
	print('selamat siang') 		#selamat siang
	print("selamat siang')		#selamat siang
	print('jum\'at')			#jum'at
	print("jum'at')				#jum'at
	print("selamat \"datang\" di indonesia")  #selamat "datang" di indonesia
	print('selamat "datang" di indonesia') #selamat "datang" di indonesia

ketika di dalam string mengunakan tanda kutip tunggal atau tanda kutip \n
ganda , gunakan tanda \ lalu diikuti kutip tunggal atau kutip ganda maka\n
akan menampilkan tanda kutip tunggal atau kutip ganda.
 
## menghilangkan tanda \ sebagai karakter special
jika kita ingin menampilkan tanda \ di dalam string gunakan fungsi \n
**print(r'...')**, fungsi ini akan menampilkan raw string contoh :\n
	
	print('c:\xampp\nama') # c:\xampp
						   # ama
	print(r'c:\xampp\nama') # c:\xampp\nama

## String dengan banyak baris 
untuk menampilkan string dengan banyak baris ada baiknya gunakan tanda 
"""...""" atau '''...'''. seperti dibahan ini : 
	
	print("""\
	Pilih menu :
	----------------------------
	1. pilihan pertama
	2. pilihan kedua
	3. pilihan ketiga
	4. keluar
	-----------------------------
	pilihan : 
	""")


## Mengabungkan (concate) dan Mengulangi String
Pengabungan 2 buah string mengunakan operator **+**, Pengulangan string 
mengunakan operator __*__.

## Index di dalam string
Setiap string di dalam python memiliki index, setiap index di mulai dari
angka 0, index bisa berupa angka negatif yang berarti perhitungan index
dimulai dari kanan.

## Memotong String (slicing string)
Menampilkan sebagian dari string bisa mengunakan index yang di butuhakan
hanya index awal dan index akhir contoh:

	word = 'belajar python'
	word[0:2]		# karakter dari posisi 0 sampai 2, tetapi tidak termasuk posisi 2

ketika hanya ingin memotong string yang sudah pasti di mulai dari index awal
bisa mengunakan cara singkat yaitu :

	word = 'belajar python'
	word[:2]		# karakter dari posisi 0 sampai 2, tetapi tidak termasuk posisi 2
	word[2:]		# karakter dari posisi 0 sampai posisi akhir dari string
	word[-2:]		# karakter dari posisi -2 sampai posisi akhir dari string
	word[:-2]		# karakter dari posisi index awal string sampai posisi -2 tidak termasuk posisi 2

## Python string abadi(immutable) tidak bisa di rubah

