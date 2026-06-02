def converter_distancia(valor, de, para):
    if de == 1:  # Metro
        metros = valor
    elif de == 2:  # KM
        metros = valor * 1000
    elif de == 3:  # Centímetro
        metros = valor / 100
    elif de == 4:  # Milímetro
        metros = valor / 1000

    if para == 1:  # Metro
        return metros
    elif para == 2:  # KM
        return metros / 1000
    elif para == 3:  # Centímetro
        return metros * 100
    elif para == 4:  # Milímetro
        return metros * 1000

def converter_moeda(valor, de, para):
    taxas = {
        1: {'BRL': 1, 'USD': 0.20, 'EUR': 0.18},  # REAL
        2: {'BRL': 5.0, 'USD': 1, 'EUR': 0.92},   # DÓLAR
        3: {'BRL': 5.45, 'USD': 1.09, 'EUR': 1}   # EURO
    }
    moedas = {1: 'BRL', 2: 'USD', 3: 'EUR'}

    usd = valor / taxas[de]['USD']
    return usd * taxas[para]['USD']

def converter_tempo(valor, de, para):
    if de == 1:  # Segundos
        segundos = valor
    elif de == 2:  # Minutos
        segundos = valor * 60
    elif de == 3:  # Horas
        segundos = valor * 3600
    elif de == 4:  # Dias
        segundos = valor * 86400

    if para == 1:  # Segundos
        return segundos
    elif para == 2:  # Minutos
        return segundos / 60
    elif para == 3:  # Horas
        return segundos / 3600
    elif para == 4:  # Dias
        return segundos / 86400

def converter_temperatura(valor, de, para):
    if de == 1:  # Celsius
        celsius = valor
    elif de == 2:  # Fahrenheit
        celsius = (valor - 32) * 5/9
    elif de == 3:  # Kelvin
        celsius = valor - 273.15

    if para == 1:  # Celsius
        return celsius
    elif para == 2:  # Fahrenheit
        return celsius * 9/5 + 32
    elif para == 3:  # Kelvin
        return celsius + 273.15

def converter_massa(valor, de, para):
    if de == 1:  # Gramas
        gramas = valor
    elif de == 2:  # Quilogramas
        gramas = valor * 1000
    elif de == 3:  # Libras
        gramas = valor * 453.592
    elif de == 4:  # Onças
        gramas = valor * 28.3495

    if para == 1:  # Gramas
        return gramas
    elif para == 2:  # Quilogramas
        return gramas / 1000
    elif para == 3:  # Libras
        return gramas / 453.592
    elif para == 4:  # Onças
        return gramas / 28.3495

conv = input('\nDIGITE QUAL A CONVERSÃO\n--------------------------------------------\n1: Distância\n2: Moeda\n3: Tempo\n4: Temperatura\n5: Massa\n--------------------------------------------\nRESPOSTA AQUI: ')

while conv not in ['1', '2', '3', '4', '5']:
    print('ERRO: CONVERSÃO INVÁLIDA')
    conv = input('\nDIGITE O NÚMERO PARA SELECIONAR A CONVERSÃO\n--------------------------------------------\n[1]Distância\n[2]Moeda\n[3]Tempo\n[4]Temperatura\n[5]Massa\n--------------------------------------------\nRESPOSTA AQUI: ')

conv = int(conv)

if conv == 1:  # Distância
    print('\nUnidades disponíveis:')
    print('1: Metro')
    print('2: Quilômetro (KM)')
    print('3: Centímetro')
    print('4: Milímetro')
    uni = input('\nEscolha a unidade de origem (1-4): ')
    while uni not in ['1', '2', '3', '4']:
        print('ERRO: UNIDADE INVÁLIDA')
        uni = input('\nEscolha a unidade de origem (1-4): ')
    uni = int(uni)

    uni2 = input('\nEscolha a unidade de destino (1-4): ')
    while uni2 not in ['1', '2', '3', '4']:
        print('ERRO: UNIDADE INVÁLIDA')
        uni2 = input('\nEscolha a unidade de destino (1-4): ')
    uni2 = int(uni2)

    valor = float(input('\nDigite o valor a ser convertido: '))

    resultado = converter_distancia(valor, uni, uni2)
    unidades = {1: 'metros', 2: 'quilômetros', 3: 'centímetros', 4: 'milímetros'}
    print(f'\n{valor} {unidades[uni]} = {resultado:.4f} {unidades[uni2]}')

elif conv == 2:  # Moeda
    print('\nMoedas disponíveis:')
    print('1: Real (BRL)')
    print('2: Dólar (USD)')
    print('3: Euro (EUR)')
    uni = input('\nEscolha a moeda de origem (1-3): ')
    while uni not in ['1', '2', '3']:
        print('ERRO: MOEDA INVÁLIDA')
        uni = input('\nEscolha a moeda de origem (1-3): ')
    uni = int(uni)

    uni2 = input('\nEscolha a moeda de destino (1-3): ')
    while uni2 not in ['1', '2', '3']:
        print('ERRO: MOEDA INVÁLIDA')
        uni2 = input('\nEscolha a moeda de destino (1-3): ')
    uni2 = int(uni2)

    valor = float(input('\nDigite o valor a ser convertido: '))

    resultado = converter_moeda(valor, uni, uni2)
    moedas = {1: 'BRL', 2: 'USD', 3: 'EUR'}
    print(f'\n{valor} {moedas[uni]} = {resultado:.2f} {moedas[uni2]}')

elif conv == 3:  # Tempo
    print('\nUnidades disponíveis:')
    print('1: Segundos')
    print('2: Minutos')
    print('3: Horas')
    print('4: Dias')
    uni = input('\nEscolha a unidade de origem (1-4): ')
    while uni not in ['1', '2', '3', '4']:
        print('ERRO: UNIDADE INVÁLIDA')
        uni = input('\nEscolha a unidade de origem (1-4): ')
    uni = int(uni)

    uni2 = input('\nEscolha a unidade de destino (1-4): ')
    while uni2 not in ['1', '2', '3', '4']:
        print('ERRO: UNIDADE INVÁLIDA')
        uni2 = input('\nEscolha a unidade de destino (1-4): ')
    uni2 = int(uni2)

    valor = float(input('\nDigite o valor a ser convertido: '))

    resultado = converter_tempo(valor, uni, uni2)
    unidades = {1: 'segundos', 2: 'minutos', 3: 'horas', 4: 'dias'}
    print(f'\n{valor} {unidades[uni]} = {resultado:.4f} {unidades[uni2]}')

elif conv == 4:  # Temperatura
    print('\nEscalas disponíveis:')
    print('1: Celsius')
    print('2: Fahrenheit')
    print('3: Kelvin')
    uni = input('\nEscolha a escala de origem (1-3): ')
    while uni not in ['1', '2', '3']:
        print('ERRO: ESCALA INVÁLIDA')
        uni = input('\nEscolha a escala de origem (1-3): ')
    uni = int(uni)

    uni2 = input('\nEscolha a escala de destino (1-3): ')
    while uni2 not in ['1', '2', '3']:
        print('ERRO: ESCALA INVÁLIDA')
        uni2 = input('\nEscolha a escala de destino (1-3): ')
    uni2 = int(uni2)

    valor = float(input('\nDigite o valor a ser convertido: '))

    resultado = converter_temperatura(valor, uni, uni2)
    escalas = {1: '°C', 2: '°F', 3: 'K'}
    print(f'\n{valor}{escalas[uni]} = {resultado:.2f}{escalas[uni2]}')

elif conv == 5:  # Massa
    print('\nUnidades disponíveis:')
    print('1: Gramas')
    print('2: Quilogramas')
    print('3: Libras')
    print('4: Onças')
    uni = input('\nEscolha a unidade de origem (1-4): ')
    while uni not in ['1', '2', '3', '4']:
        print('ERRO: UNIDADE INVÁLIDA')
        uni = input('\nEscolha a unidade de origem (1-4): ')
    uni = int(uni)

    uni2 = input('\nEscolha a unidade de destino (1-4): ')
    while uni2 not in ['1', '2', '3', '4']:
        print('ERRO: UNIDADE INVÁLIDA')
        uni2 = input('\nEscolha a unidade de destino (1-4): ')
    uni2 = int(uni2)

    valor = float(input('\nDigite o valor a ser convertido: '))

    resultado = converter_massa(valor, uni, uni2)
    unidades = {1: 'gramas', 2: 'quilogramas', 3: 'libras', 4: 'onças'}
    print(f'\n{valor} {unidades[uni]} = {resultado:.4f} {unidades[uni2]}')

print('\nConversão realizada com sucesso!')

