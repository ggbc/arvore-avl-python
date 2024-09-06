nome = "GUSTAVO"
nome2 = "GUSTAVO"

print(nome == nome2) #True, conteúdos iguais!
print(nome is nome2) #True!!!! Com strings, existe otimização de memória. O objeto de referência é o mesmo.
print(nome.lower() == nome2) #False. conteúdos distintos
print(nome.lower() is nome2) #False. lower() cria uma nova string 
print(nome.lower() == nome2.lower()) #True. conteúdos iguais!
print(nome.lower() is nome2.lower()) #False. lower() cria objetos distintos em ambos os casos

c = [10, 20, 30] 
print(type(c))
d = [10, 20, 30]
print(type(d))

print (c == d) #True. Conteúdos iguais!
print (c is d) #False. Não se trata de strings, portanto são áreas de memória distintas