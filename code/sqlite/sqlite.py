import sqlite3

# 1. Membuat Database
koneksi = sqlite3.connect('test.db')
print("Sukses Open database !")

# 2. Membuat Tabel
# koneksi.execute('''
# CREATE TABLE penghuni (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT UNIQUE NOT NULL,
#     nama TEXT NOT NULL,
#     di_rumah TEXT NOT NULL,
#     create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
# );''')
# print("Berhasil membuat tabel")

# 3. Menambah Data
# koneksi.execute("INSERT INTO penghuni (username, nama, di_rumah) \
#                  VALUES ('oky31','oky saputra','ya')")

# koneksi.execute("INSERT INTO penghuni (username, nama, di_rumah) \
#                  VALUES ('edy','susilo nofiadi','ya')")

# koneksi.execute("INSERT INTO penghuni (username, nama, di_rumah) \
#                  VALUES ('tama','Arya pratam','tidak')")

# koneksi.commit()
# print("Berhasil Memasukan Data")


# 4. Select data
# cursor = koneksi.execute("SELECT * FROM penghuni")

# for row in cursor:
#     print("ID = ", row[0])
#     print("username = ", row[1])
#     print("nama = ", row[2], '\n')

# print('Sukses Select data')

# 5. Update Data
# koneksi.execute("UPDATE penghuni set nama = 'oky nubs' WHERE  id=1")
# koneksi.commit

# cursor = koneksi.execute("SELECT * FROM penghuni")

# for row in cursor:
#     print("ID = ", row[0])
#     print("username = ", row[1])
#     print("nama = ", row[2], '\n')
# print("Total baris yang di update :", koneksi.total_changes)


# 6. Delete Data
# koneksi.execute("DELETE FROM penghuni WHERE id = 3")
# koneksi.commit()
# print("Total baris yang di hapus ", koneksi.total_changes)

# cursor = koneksi.execute("SELECT * FROM penghuni")

# for row in cursor:
#     print("ID = ", row[0])
#     print("username = ", row[1])
#     print("nama = ", row[2], '\n')

koneksi.close()