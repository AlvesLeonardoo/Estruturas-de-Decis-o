num = input()
a, b, c = num.split()
a, b, c = int(a), int(b), int(c)
def Ordena(a,b,c):
  lista = [a,b,c]
  maiorNumero = max(lista)
  menorNumero = min(lista)
  lista.remove(maiorNumero)
  lista.remove(menorNumero)
  meioNumero = lista[0]
  return f'({menorNumero}, {meioNumero}, {maiorNumero})'
print(Ordena(a,b,c))