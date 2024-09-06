""" inteiros = [1, 2, 3, 4, 5, 6]
ints = [88, 56, 34, 76, 3]

print(inteiros[2])
print(inteiros[-2]) #de trás para frente


#print(ints ** 2) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
print(ints *2) #não multiplica cada int; duplica os itens na lista.

print(ints + ints) #faz a mesma coisa que print(ints * 2)

#print(inteiros / 2) #TypeError: unsupported operand type(s) for /: 'list' and 'int'
#print(ints - 2) #TypeError: unsupported operand type(s) for -: 'list' and 'int'
#print(ints + 2) #TypeError: can only concatenate list (not "int") to list

ints += [20]
print(ints) """

ints = [4, 56, 34, 76, 3]
L = ints[0] * [17]
print(L)
print(ints[0] * 17)

print(type(L))
print(0 in L)

Abc = ["oi", 34]
print(type(Abc))

print("oi" in Abc)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(type(thisdict))