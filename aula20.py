number1 = input("Digite um valor: ")
number2 = input("Digite outro valor: ")

num1 = int(number1)
num2 = int(number2)

if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 < num2:
    print(f"{num2} é maior que {num1}")
else:
    print("Valores são iguais")


str1 = "{numero1} é maior que {numero2}"
str2 = "{numero2} é maior que {numero1}"

if num1 > num2:
    print(str1.format(numero1 = num1, numero2 = num2))
elif num1 < num2:
    print(str2.format(numero1 = num1, numero2 = num2))
else:
    print("Valores são iguais")
