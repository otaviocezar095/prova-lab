def soma_diagonal_principal(matriz):
    soma = 0 
    for i in range(len(matriz)):
        soma += matriz[i][i]
        return soma

#b)
def soma_diagonal_principal(matriz):
    soma = 0 
    for i in range(len(matriz)):
        soma += matriz[i][-i]
        return soma

#c)
def soma_diagonal_principal(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
            return soma

#d) 
def soma_diagonal_principal(matriz):
    soma = 0 
    for i in range(len(matriz)):
        soma += matriz[1][len(matriz)-i-1]
        return soma

#e)
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[len(matriz)-i-1][1]
        return soma