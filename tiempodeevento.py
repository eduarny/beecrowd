a = int(input("Dia "))
linea1 = input()
array1 = linea1.split(' : ')
x = int(array1[0])
y = int(array1[1])
z = int(array1[2])

b = int(input("Dia "))
linea2 = input()
array2 = linea2.split(' : ')
p = int(array2[0])
q = int(array2[1])
r = int(array2[2])

resultado2 = (b * 86400) + (p * 3600) + (q * 60) + r
resultado1 = (a * 86400) + (x * 3600) + (y * 60) + z
respuesta = resultado2 - resultado1

if a<=b:
    if x<=p and y<=q and z<=r:
        respuesta = respuesta
        dias = respuesta // 86400
        horas = (respuesta - (dias * 86400)) // 3600
        minutos = ((respuesta - (dias * 86400)) - (horas * 3600)) // 60
        segundos = (((respuesta - (dias * 86400)) - (horas * 3600)) - (minutos * 60))
    else:
        respuesta = respuesta
        dias = respuesta // 86400
        horas = (respuesta - (dias * 86400)) // 3600
        minutos = ((respuesta - (dias * 86400)) - (horas * 3600)) // 60
        segundos = (((respuesta - (dias * 86400)) - (horas * 3600)) - (minutos * 60))

print(str(dias) + ' dia(s)')
print(str(horas) + ' hora(s)')
print(str(minutos) + ' minuto(s)')
print(str(segundos) + ' segundo(s)')