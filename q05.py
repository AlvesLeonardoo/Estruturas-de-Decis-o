litros = input()
n,a,b = litros.split()
n,a,b = int(n), int(a), int(b)
def dinheiros(n,a,b):
    if a < b:
      print(n*a)
    else:
      print((n//2)*b+(n%2)*a)
dinheiros(n,a,b)  