import math

radius = float(input("masukan jari-jari tabung:"))
tinggi = float(input("masukan tinggi tabung:"))
volume = math.pi *radius**2 * tinggi
print(f"volume tabung dengan jari-jaari {radius} dan tinggi{tinggi} adalah {volume}")
