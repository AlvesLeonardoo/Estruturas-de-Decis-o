nums = input()
a, b, c = nums.split()
a, b, c = int(a), int(b), int(c)
def realidade(a,b,c):
    result = b**2 - 4*a*c
    if result >=0:
      print('reais')
    else:
      print('complexas')
realidade(a,b,c)