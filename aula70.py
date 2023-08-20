
def somar(x,y):
    return x + y
    print(x + y) # codigo é inalcançável, porque return foi escrito antes. "print()" eh uma função que retorna None

variavel = somar(5, 7)
print(variavel)

def somar2(x,y,*args): # desempacotamento, para isso usamos a tupla *args, usando desempacotamento, podemos passar quantos argumentos for preciso
    aux = 0
    for num in args:
        aux += num
    return aux

variavel2 = somar2(5,6,8,9,7,5,1,10)
print(variavel2)