soma=0
while True:
    nota1=float(input("Digite a primeira nota: ").replace(',','.'))
    if nota1>0 and nota1<=10:
        soma+=nota1
        print("\n")
        break
while True:
    nota2=float(input("Digite agora a segunda nota: ").replace(',','.'))
    if nota2>0 and nota2<=10:
        soma+=nota2
        break
media = soma/2
print(f"\nA média do aluno foi {media}\nNota 1: {nota1}\nNota 2: {nota2}")


