
def multiplicaArgs(*args):
    aux = 1
    for num in args:
        if num == 0:
            print("possui \"0\" nos argumentos")
            return 0
        else:
            aux*=num
    return aux

result_mult = multiplicaArgs(10,9,8,7,5)

print(result_mult)

def par_ou_impar(num):
    return f"{num} é par" if (num % 2 == 0) else f"{num} é ímpar"

print(par_ou_impar(6))