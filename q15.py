def piscininha(x, y, w, h, a, b):
  if x < a < (x + w) and y < b < (y + h):
    print('Dando um tchibum')
  elif x <= a <= (x + w) and y <= b <= (y + h):
    print('So com os pezin dentro da agua')
  else:
    print('Tomando um solzin')