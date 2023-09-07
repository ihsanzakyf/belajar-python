a = 10
b = 3

# Operasi Tambah +
hasil = a + b
print(a,"+",b,"=",hasil)

# Operasi Pengurangan -
hasil = a - b
print(a,"-",b,"=",hasil)

# Operasi Perkalian *
hasil = a * b
print(a,"x",b,"=",hasil)

# Operasi Pembagian /
hasil = a / b
print(a,"/",b,"=",hasil)

# Operasi Modulus %
hasil = a % b
print(a,"%",b,"=",hasil)

# Operasi Eksponen (pangkat) **
hasil = a ** b
print(a,"^",b,"=",hasil)

# Operasi Floor Division //
hasil = a // b
print(a,"//",b,"=",hasil)

# Prioritas Operasi
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print( x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil)

hasil = (x + y) * z
print("(",x,"+",y,") x",z,"=",hasil)