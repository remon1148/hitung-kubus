#menghitungkpk dan fpb
import math

angka1 = int(input("masukan angka pertama:"))
angka2 = int(input("masukan angka kedua:"))

fpb =math.gcd(angka1, angka2)
kpk = (angka1 * angka2 ) // fpb

print(f"FPB dari {angka1} dan {angka2} adalah {fpb}")
print(f"KPK dari {angka1} dan {angka2} adalah {kpk}")