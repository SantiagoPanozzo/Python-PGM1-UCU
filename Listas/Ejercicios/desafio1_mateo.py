def d_verificador(ci):
    lista=[]
    ci=int(ci)
    if ci > 100000 and ci < 9999999:
        ci=str(ci)
        for i in ci:
            lista.append(i)
        total=(int(lista[-1])*4)+(int(lista[-2])*3)+(int(lista[-3])*6)+(int(lista[-4])*7)+(int(lista[-5])*8)+(int(lista[-6])*9)+(int(lista[-7])*2)
        casi=total%10
        digito=10-casi

        return digito
    else:
        print("La Cedula es invalida")

def verificador(ci,digito):
    verify = d_verificador(ci)
    if digito==verify:
        return True
    else:
        return False
a=""

ci=input("Ingresa tu CI (sin el ultimo dígito): ")
print('El último dígito de tu CI es:',d_verificador(ci))

digito=int(input('Ingresa el verificador: '))
print(verificador(ci,digito))
