repetir ="s"

while repetir=="s":
    while True:
        nota1 = float(input("Digite a primeira nota: ").replace(',', '.'))
        if nota1 >= 0 and nota1 <= 10:
            break
    while True:
        nota2 = float(input("Digite agora a segunda nota: ").replace(',', '.'))
        if nota2 >= 0 and nota2 <= 10:
            break
    media = (nota1 + nota2) / 2
    print(f"\nA média do aluno foi {media}\nNota 1: {nota1}\nNota 2: {nota2}")
    repetir = input("\nDeseja realizar novo calculo? S- Sim N-Não: ").lower()


