def MostrarReceta(cant,unit,ingr,procd):
    if not (len(cant) == len(unit) == len(ingr)):
        return print('Error, el número de elementos no es el mismo en cada lista')
    print('Ingredientes:')
    for i in range(len(cant)):
        print(f'    {cant[i]} {unit[i]} de {ingr[i]}')
    print(f'Procedimiento:\n    {procd}')


cant = [100,50,1]
unit = ["g", "ml", "unidades"]
ingr = ["Harina", "Leche", "Huevo"]
procd = "Mezclar todo, dejar reposar y cocinar"
MostrarReceta(cant,unit,ingr,procd)