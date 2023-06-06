n = int(input())
def EhBissexto(n):
  if n%4==0 and n%100!=0 or n%400==0:
    print('Bissexto') #usar return no aprender3 
  else: 
    print('Ano Comum') #usar return no aprender3 
EhBissexto(n)