medidas = input()
a, b, c = medidas.split()
def classificador(a,b,c):
  lista = [a,b,c]
  maiornumero = max(lista)
  lista.remove(maiornumero)
  ladoa = lista[0]
  ladob = lista[1]
  
  if maiornumero < ladoa + ladob and abs(ladoa - ladob)< maiornumero:
    print('triangulo')
    if a != b and b != c and c != a:
      print('escaleno')
    if a == b or b == c or c == a:
      print('isosceles')
    if a == b and b == c:
      print('equilatero')
    if maiornumero**2 == ladoa**2 + ladob**2:
      print('retangulo')
  else:
    print('gondim sendo gondim')
classificador(a,b,c)