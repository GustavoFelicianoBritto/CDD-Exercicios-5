cont=1
target=10
notaSoma=0

while cont <= target:
    num = float(input(f"Digite a {cont}ª nota: ").replace(',','.'))
    notaSoma+=num
    cont+=1

media = notaSoma/target

print(f"A sua média foi: {media:.2f}")