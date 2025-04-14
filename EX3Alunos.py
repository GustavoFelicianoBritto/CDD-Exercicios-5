AlunosQtd= int(input("Digite a quantidade de alunos da turma: "))
cont = 1
soma=0
while cont <= AlunosQtd:
    nota= float(input(f"Digite a nota do {cont}º aluno: ").replace(',','.'))
    soma +=nota
    cont+=1

media = soma/AlunosQtd

print(f"A média da turma é: {media:.2f}")
