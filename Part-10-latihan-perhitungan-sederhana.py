# latihan konversi satuan temperature

# program konversi celcius ke satuan

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam celcius :'))
print("suhu adalah",celcius, "Celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "kelvin")