cartas = input()
a, b = cartas.split()
a , b = int(a), int(b)
def jogadas(a,b):
  if a == b:
    print(0)
  elif (abs(a-b)%10) == 0:
    print(abs(a-b)//10)
  else:
    print((abs(a-b)//10)+1)
jogadas(a,b)