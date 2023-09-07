## Casting Tipe Data
# Merubah dari suatu tipe data ke tipe data lainnya
# Tipe Data: data_int. data_float, data_str, data_bool

# Ini adalah data integer
print("")
print("=====INTEGER=====")
print("")
data_int = 23
print("isi datanya adalah integer :", data_int)
print("- tipe datanya adalah :", type(data_int))

data_float = float(data_int)
print("kemudian dirubah menjadi float hasilnya adalah :", data_float)
print("- tipe datanya adalah :", type(data_float))

data_str = str(data_int)
print("kemudian dirubah menjadi string hasilnya adalah :", data_str)
print("- tipe datanya adalah :", type(data_str))

data_bool = bool(data_int)
print("kemudian dirubah menjadi boolean hasilnya adalah :", data_bool)
print("- tipe datanya adalah :", type(data_bool))

# Ini adalah data float
print("")
print("=====FLOAT=====")
print("")
data_float = 2.3
print("isi datanya adalah float :", data_float)
print("- tipe datanya adalah :", type(data_float))

data_int = int(data_float)
print("kemudian dirubah menjadi integer hasilnya adalah :", data_int)
print("- tipe datanya adalah :", type(data_int))

data_str = str(data_float)
print("kemudian dirubah menjadi string hasilnya adalah :", data_str)
print("- tipe datanya adalah :", type(data_str))

data_bool = bool(data_float)
print("kemudian dirubah menjadi boolean hasilnya adalah :", data_bool)

# Ini adalah data boolean
print("")
print("=====BOOLEAN=====")
print("")
data_bool = False
print("isi datanya adalah boolean :", data_bool)
print("- tipe datanya adalah :", type(data_bool))

data_int = int(data_bool)
print("kemudian dirubah menjadi integer hasilnya adalah :", data_int)
print("- tipe datanya adalah :", type(data_int))

data_str = str(data_bool)
print("kemudian dirubah menjadi string hasilnya adalah :", data_str)
print("- tipe datanya adalah :", type(data_str))

data_float = float(data_bool)
print("kemudian dirubah menjadi float hasilnya adalah :", data_float)
print("- tipe datanya adalah :", type(data_float))

# Ini adalah dara string
print("")
print("=====STRING=====")
print("")
data_str = "Halo, nama saya Ihsan Zaky Fadillah"
print("ini datanya adalah string", data_str)
print("- tipe datanya adalah", type(data_str))

data_int = int(data_str) # String harus angka
print("Kemudian dirubah menjadi integer hasilnya adalah :", data_int)
print("- tipe datanya adalah :", type(data_int))

data_float = float(data_str) # String harus angka
print("Kemudian dirubah menjadi float hasilnya adalah :", data_float)
print("- tipe datanya adalah :", type(data_float))

data_bool = bool(data_str) # False jika string kosong
print("Kemudia dirubah menjadi data boolean hasilnya adalah", data_bool)
print("- tipe datanya adalah :", type(data_bool))