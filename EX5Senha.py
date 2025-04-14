user = "User00"
password = "123456"
error = 3

while error>0:
    passwordInput = input(f"Olá, {user} Por favor, digite sua senha (tentativas restantes {error}: ")
    if passwordInput == password:
        print(f"\n===========\nUsuário logado\n===========")
        break
    else:
        error-=1
        if error<=0:
            print("Tentativas excedidas, conta bloqueada!!!")



