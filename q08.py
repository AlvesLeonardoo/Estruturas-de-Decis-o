medidas = input()
a, b, c = medidas.split()
def formamisteriosa(a,b,c):
  lista = [a,b,c]
  maiornumero = max(lista)
  lista.remove(maiornumero)
  ladoa = lista[0]
  ladob = lista[1]

  if a == b:
    print('pode ser quadrado')
  if a != b:
    print('pode ser retangulo')
  
  if maiornumero < ladoa + ladob and abs(ladoa - ladob)< maiornumero:
    if a != b and b != c and c != a:
      print('pode ser triangulo escaleno')
    elif a == b and b == c:
      print('pode ser triangulo equilatero')
    elif a == b and b != c or b == c and c != a or c == a and a != b:
      print('pode ser triangulo isosceles')
formamisteriosa(a,b,c)