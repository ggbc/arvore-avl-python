data = {2, 4, 6, 8}
dados = [2,4,6,8]
def sopares(dados):
    for i in range(len(dados)):
        if dados[i] % 2 != 0:
            return False
    return True
print(type(dados))
print(len(dados))
print (sopares(dados))



print(type(data))
print(len(data))