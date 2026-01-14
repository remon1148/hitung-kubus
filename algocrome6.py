#menampilkan tabel perkalian
angka = int(input("masukan angka yang ingin dikalihkan anda:"))

for i in range (1, 11):
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")
