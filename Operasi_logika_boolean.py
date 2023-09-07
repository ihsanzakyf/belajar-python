# Operasi logika atau boolean
# not, or, and xor

## NOT
print("\n=====NOT=====\n")
a = True
c = not a
print("Data a =", a)
print("-----------NOT")
print("Data c =", c)

## OR
# Jika salah satu True, maka hasilnya True
print("\n=====OR=====\n")
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

## AND
# Jika salah satu True, maka hasilnya False
print("\n=====AND=====\n")
a = False
b = False
c = a and b
print(a, 'and', b, '=', c)
a = False
b = True
c = a and b
print(a, 'and', b, '=', c)
a = True
b = False
c = a and b
print(a, 'and', b, '=', c)
a = True
b = True
c = a and b
print(a, 'and', b, '=', c)

## XOR
# Akan true jika salah satu true, dan jika keduanya sama maka akan false
print("\n=====XOR=====\n")
a = False
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'xor', b, '=', c)