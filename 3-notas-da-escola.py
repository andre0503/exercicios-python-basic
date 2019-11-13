notas = []
contador = 0

while contador < 4:
    nota = float(input("digite nota "))
    contador += 1
    notas.append(nota)
media = (notas[0] + notas[1] + notas[2] + notas[3])/4
print(media)

if media >= 5:
    print("você está aprovado")

else:
    print("você está reprovado")
