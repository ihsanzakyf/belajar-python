## Input dari user
print("")
print("====FORM SEDERHANA====")
print("")
data = input("Masukan nama: ")
print("Nama kamu adalah = ", data)
print("Typenya adalah ", type(data))
print("======================")
# Jika ingin mengambil int
data_int = int(input("Masukan umur: "))
print("Umur kamu adalah = ", data_int)
print("Typenya adalah ", type(data_int))
print("======================")
data_boolean = bool(int(input("Masukan nilai boolean: ")))
print("Nilai boolean = ", data_boolean)
print("Typenya adalah = ", type(data_boolean))