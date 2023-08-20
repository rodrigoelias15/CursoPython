
def multiplicacao(multiplicador):
    def resultado(num):
        return multiplicador * num
    return resultado

result1 = multiplicacao(3)
print(result1(5))

result2 = multiplicacao(3)(5) # parâmetro externo e mais interno respectivamente
print(result2)