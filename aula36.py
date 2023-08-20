cont = 0

while cont < 20:
    cont+=1
    if cont == 15:
        cont+=1
        continue # retorna para início do laço (while)
    
    
    print(cont, end=" ")