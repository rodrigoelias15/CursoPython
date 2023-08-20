while True:
    
    sair = input("Quer sair? Digite 's' para 'sim' ").lower().startswith("s") # retorna bool
    
    if sair is True:
        break
    else:        
        num1_float = None
        num2_float = None
        
        try:
            num1 = input("Digite um número: ")
            num2 = input("Digite outro número: ")
            operador = input("Digite um operador (+ - * /): ")
            
            num1_float = float(num1)
            num2_float = float(num2)
            if operador == "+":
                resultado = num1_float + num2_float
                print(f"Resultado da sua soma = {resultado}")
                break
            elif operador == "-":
                resultado = num1_float - num2_float
                print(f"Resultado da sua subtração = {resultado}")
                break
            elif operador == "*":
                resultado = num1_float * num2_float
                print(f"Resultado da sua multiplicação = {resultado}")
                break
            elif operador == "/":
                resultado = num1_float / num2_float
                print(f"Resultado da sua divisão = {resultado}")
                break
        except:
            print(f"Valor do primeiro número digitado: {num1_float}")
            print(f"Valor do segundo número digitado: {num2_float}")
            break