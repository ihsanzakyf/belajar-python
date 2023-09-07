# tipe data: integer
data_integer = 11
print("data :", data_integer)
print("- bertipe :", type(data_integer))

# tipe data: float
data_float = 1.9
print("data :", data_float)
print("- bertipe :", type(data_float))

# tipe data: string
data_str = "Ihsan Zaky Fadillah"
print("data :", data_str)
print("- bertipe :", type(data_str))

# tipe data: boolean / biner = 0 /1
data_bool = True
print("data :", data_bool)
print("- bertipe :", type(data_bool))

## Tipe data khusus
# Bilangan kompleks
data_complex = complex(5, 6)
print("data :", data_complex)
print("- bertipe :", type(data_complex))

# Tipe data dari bahasa C
from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe :", type(data_c_double))