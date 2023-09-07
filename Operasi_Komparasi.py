# Operasi Komparasi
# Setiap hasil dari operasi komparasi adalah boolean jadi ada True atau False
# >,<,>=,<=,==,!=,is,is not


a=4
b=2
# Lebih besar dari >
print("\n=====LEBIH BESAR DARI (>)=====\n")
hasil = a > b
print(a,">",b,"=",hasil)
hasil = a > b
print(a,"<",b,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# Kurang dari <
print("\n=====KURANG DARI (<)=====\n")
hasil = a < 7
print(a,"<",7,"=",hasil)
hasil = a < b
print(a,"<",b,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# Lebih dari sama dengan >=
print("\n=====LEBIH DARI SAMA DENGAN (>=)=====\n")
hasil = a >= b
print(a,">=",b,"=",hasil)
hasil = a >= b
print(a,">=",b,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# Kurang dari sama dengan <=
print("\n=====KURANG DARI SAMA DENGAN (<=)=====\n")
hasil = a <= b
print(a,"<=",b,"=",hasil)
hasil = a <= b
print(a,"<=",b,"=",hasil)
hasil = b <= 2
print(b,"<=",2,"=",hasil)

# Sama dengan ==
print("\n=====SAMA DENGAN (==)=====\n")
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = b == 4
print(b,"==",4,"=",hasil)

# Tidak dengan !=
print("\n=====TIDAK DENGAN (!=)=====\n")
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = b != 4
print(b,"!=",4,"=",hasil)

# IS sebagai komparasi objek identity
x = 5 # ini adalah assignment membuat objek
y = 5
print("\n=====OBJECT INDENTITY(is)=====\n")
print('nilai x =', x, ', id =', hex(id(x)))
print('nilai y =', y, ', id =', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

x = 5 # ini adalah assignment membuat objek
y = 7
print("\n=====OBJECT INDENTITY(is not)=====\n")
print('nilai x =', x, ', id =', hex(id(x)))
print('nilai y =', y, ', id =', hex(id(y)))
hasil = x is not y
print('x is y = ', hasil)

