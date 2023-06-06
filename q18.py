n = int(input())
def NomeMes(n):
  if n == 1:
    return 'Janeiro'
  elif n == 2:
    return 'Fevereiro'
  elif n == 3:
    return 'Março'
  elif n == 4:
    return 'Abril'
  elif n == 5:
    return 'Maio'
  elif n == 6:
    return 'Junho'
  elif n == 7:
    return 'Julho'
  elif n == 8:
    return 'Agosto'
  elif n == 9:
    return 'Setembro'
  elif n == 10:
    return 'Outubro'
  elif n == 11:
    return 'Novembro'
  elif n == 12:
    return 'Dezembro'
  else:
    return 'Mês inválido'
NomeMes(n)