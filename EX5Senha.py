user = "User00"
password = "123456"
error = 3

while error>0:
    passwordInput = input(f"Olá, {user} Por favor, digite sua senha (tentativas restantes {error}): ")
    if passwordInput == password:
        print(f"\n{"="*30}\nUsuário logado\n{"="*30}")
        break
    else:
        error-=1
        if error<=0:
            print(f"\n{"="*30}\nTentativas excedidas, conta bloqueada!!!\n{"="*30}\n")



