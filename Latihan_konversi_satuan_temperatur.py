# Latihan konversi satuan temperatur

# Program konversi celcius le satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print('Suhu adalah : ', celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print('Suhu dalam reamur adalah : ', reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print('Suhu dalam fahrenheit dalah : ', fahrenheit, "Fahrenheit")


# Kelvin
kelvin = celcius + 273
print('Suhu dalam kelvin adalah : ', kelvin, "Kelvin")

print("\nPROGRAM KONVERSI Fahrenheit To Kelvin\n")

# Fahrenheit to Kelvin
fahrenheit = float(input("Masukan satuan dalam fahrenheit : "))
celcius = (5/9)*(fahrenheit-32)
kelvin = celcius + 273
print("Suhu dalam kelvin adalah :", kelvin, "K")

print("\nPROGRAM KONVERSI Kelvin To Fahrenheit\n")

# Kelvin to Fahrenheit
kelvin = float(input("Masukan satuan dalam kelvin :"))
celcius = kelvin-273
fahrenheit = ((9/5)*celcius) + 32
print("Suhu dalam fahreinheit adalah :", fahrenheit, "F")