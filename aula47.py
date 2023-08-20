import os

palavra_secreta = "forrozinho"
letra_acertada = ''

while True:
    letra_digitada = input("Digite uma letra: ")
    
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue
    
    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada
        
    palavra_formada = ''
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print("Você acertou!")
        os.system("clear")
        break