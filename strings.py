#Strings
#concatenação
idade = 10
print ("sua idade é " + str(idade))

#print (idade + ": anos") ---> erro de compilação: não existe operador + para (int + str)!
print (str(idade) + ": anos")



nome = "gustavo guerreiro basilio   costa   "
print("o tipo do nome é : " + str(type(nome)))

print(nome)
print(nome[0])
print(nome[len(nome)-1]) 
 
print('a' in nome) #o caracter está contido na string?
print('A' in nome) #mesma coisa, mas maiúscula

print(nome.capitalize())
print(nome[6].capitalize())
print(nome.split()) #quebra a string em substrings, usando o char 'sep' informado. 
print(nome.strip() + '.') #tira espaços do inicio e fim da string

print(nome.find('gue')) #indice da primeira vez que a substr foi encontrada

print(nome.title()) #é o capitalized() em cada primeira letra da string

print(nome.count('g'))
print(len(nome))

""" Immutable """
nome = "GUERREIRO"
nome.lower()
print(nome)
print(nome.lower())

nome2 = nome

print(nome == nome2)
print(nome is nome2)