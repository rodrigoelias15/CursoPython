# constantes são escritas em letras maiúsculas
# variáveis possuem inicial minúscula
# nos dois casos podemos usar snake case

velocidade_carro = 61
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima para o radar
LOCAL_1 = 100 # local do radar na estrada
RADAR_RANGE = 1 # local onde radar multa

vel_carro_pass_radar_1 = velocidade_carro > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) # "\" significa que código vai continuar na linha de baixo
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')

