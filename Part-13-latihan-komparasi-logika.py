# episode latihan logika dan komparasi

# membuat gabungan area rentang dari sebuah angka

# ++++++3--------10++++++++

inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3 atau \nlebih besar dari 10\n:"))

# +++++3------------------
# ,Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =",isKurangDari)

# ---------------10++++++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10=",isLebihDari)

# ++++++3--------10++++++++

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan :", isCorrect)


#------------3++++++++++++10----------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

#-------------3+++++++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ",isLebihDari)
# ++++++++++++++10------------
# kurang dari 10
isKurangDari = inputUser < 10
print("kurang dari 10 =",isKurangDari)

# ----------3++++++++10----------
isCorrect - isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorrect)