cpf = "74682489070"
i = 0
digito = 0
num = 10
digitoCPF = 0
qtdDigitosCPF = len(cpf)-2

while i < qtdDigitosCPF:
    digitoCPF = int(cpf[i])
    digito += digitoCPF * num
    i+=1
    num-=1

digito *= 10
digito %= 11

digito = 0 if digito > 9 else digito
    
print(digito)