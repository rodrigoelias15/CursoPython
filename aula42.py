str = "huehuhhhheuheesssaaaa"

letra_atual = ''
qtd_total_letras = 0
i = 0

while i < len(str):
    letra_atual = str[i].lower()
    freq_letra_atual = str.count(letra_atual)
    
    if letra_atual == ' ':
        i+=1
        continue
        
    if freq_letra_atual >= qtd_total_letras:
        qtd_total_letras = freq_letra_atual
        letra_com_mais_freq = letra_atual
    else:
        i+=1
        continue
    
    i+=1    

print(f"Letra que mais aparece é \"{letra_com_mais_freq}\", aparecendo {qtd_total_letras}x")