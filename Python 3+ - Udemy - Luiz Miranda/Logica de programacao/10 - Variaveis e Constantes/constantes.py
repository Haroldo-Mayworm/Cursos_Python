"""
CONSTANTE = "Variáveis" que não vão mudar
"""

velocidade = 100
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

acima_do_limite = velocidade > RADAR_1
dentro_do_alcance = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE)
passou_pelo_radar = local_carro > (LOCAL_1 + RADAR_RANGE)
foi_multado = dentro_do_alcance and acima_do_limite

if acima_do_limite:
    print(f"Velocidade: {velocidade} km/h — limite: {RADAR_1} km/h")

if dentro_do_alcance:
    print(f"Carro está no alcance do radar (posição {local_carro})")

if foi_multado:
    print(f"Carro multado! {velocidade - RADAR_1} km/h acima do limite")

if passou_pelo_radar and not acima_do_limite:
    print(f"Carro passou pelo radar sem multa")

if passou_pelo_radar and acima_do_limite:
    print(f"Carro passou pelo radar acima do limite")
