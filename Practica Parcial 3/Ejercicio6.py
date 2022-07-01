def promedios(lista:list,indices:list):
  p = None
  suma=0
  for i in indices:
    try: suma = suma+lista[i]
    except: pass
  try: p=suma/len(indices)
  except: pass
  return p

print(promedios([5, 8, 2, 1, 0, 7], [7, 1, 0]))
print(promedios([5, 8, 2, 1, 0, 7], []))