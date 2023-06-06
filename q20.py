medidas = input()
A, B, C = medidas.split()
A, B, C = int(A), int(B), int(C)
def EhRetangulo(A,B,C):
    lista = [A,B,C]
    maiorNumero = max(lista)
    lista.remove(maiorNumero)
    cateto1 = lista[0]
    cateto2 = lista[1]
    if maiorNumero**2 == cateto1**2 + cateto2**2:
        return 1
    else:
        return 0    
EhRetangulo(A,B,C)