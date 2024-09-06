#tipos
print("****TIPOS DOS DADOS****")
idadeInt = 42
print(type(idadeInt))
idadeStr = '42'
print(type(idadeStr))

idadeInt = idadeStr
print(type(idadeInt))

print("****CONVERSÃO DE TIPOS ****")
a = 10
b = "maria"
print(a)
print(b)
print("tentando fazer b + a - resultado esperado: não compila!")
#c = b + a #não compila!!!!! Python não tem conversaõ de tipos automática
print("tentando fazer a + b - resultado esperado: não compila")
#c = a + b
#print(c) #quando c não foi inicializada ("definida"), acontece uma exceção: NameError "name c is not defined"


#FLOAT
"""print("%.1f" % 12.45667)
print('---')
print("{:.1f}".format(12.45667))
print(f"{12.45667:.1g}")
print(f"{12.45667:.1e}")
print(round(12.45667,0))
print("%1f" % 12.45667)
print('---')"""


print('{:f}'.format(12389054))

#operações, incrementos etc
""" idade = 10
print(idade)
idade = idade + 1
print(idade)
idade += 1
print(idade)
print(++idade) #funciona, mas não é incremento. 
# na prática o interpretador entende que são dois sinais de +. 
# 1º sinaliza um incremento da parcela '+idade' que vem na sequencia do +
# 2º indica que o valor a seguir é positivo ("+idade")
# print(idade++) # já nessa linha o compilador dá erro porque python não tem pós- (nem pré-) incremento: "SyntaxError: invalid syntax"
print(+-idade)
+-idade
print(idade) """



frutas = ["maçã", "banana", "uva", "pera","morango", "melao", "mamão"]
print(frutas)
frutas_2 = set(frutas[1:5])
print(frutas_2)
frut = frutas[1:5]
print(frut)


frutas_3 = {
 "cesta_1": frutas[:2],
 "cesta_2": frutas[-3:]
}
novas_frutas = frutas[1:-1]
frutas_2.add("banana")
frutas_3["cesta_3"] = frutas[2:4]
print(frutas)
print(frutas_2)
print(frutas_3)
print(novas_frutas)