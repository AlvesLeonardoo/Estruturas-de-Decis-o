def quantosJantam(n, g, f, c):
  if g > f:
    if (f+c) < n:
      print(f+c)
    else:
      print(n)
  elif f > g:
    if (g+c) < n:
      print(g+c)
    else:
      print(n)
  else:
    if (g+c) < n:
      print(g+c)
    else:
      print(n)