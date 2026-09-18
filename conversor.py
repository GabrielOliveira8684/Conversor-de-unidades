def converter_distancia(valor, de, para):
    if de == 1:  # Metro
        metros = valor
    elif de == 2:  # KM
        metros = valor * 1000
    elif de == 3:  # Centímetro
        metros = valor / 100
    elif de == 4:  # Milímetro
        metros = valor / 1000

    if para == 1:
        return metros
    elif para == 2:
        return metros / 1000
    elif para == 3:
        return metros * 100
    elif para == 4:
        return metros * 1000

def converter_moeda(valor, de, para):
    taxas = {
        1: {'USD': 0.20},
        2: {'USD': 1},
        3: {'USD': 1.09}
    }
    usd = valor / taxas[de]['USD']
    return usd * taxas[para]['USD']

def converter_tempo(valor, de, para):
    if de == 1:
        segundos = valor
    elif de == 2:
        segundos = valor * 60
    elif de == 3:
        segundos = valor * 3600
    elif de == 4:
        segundos = valor * 86400

    if para == 1:
        return segundos
    elif para == 2:
        return segundos / 60
    elif para == 3:
        return segundos / 3600
    elif para == 4:
        return segundos / 86400

def converter_temperatura(valor, de, para):
    if de == 1:
        celsius = valor
    elif de == 2:
        celsius = (valor - 32) * 5/9
    elif de == 3:
        celsius = valor - 273.15

    if para == 1:
        return celsius
    elif para == 2:
        return celsius * 9/5 + 32
    elif para == 3:
        return celsius + 273.15

def converter_massa(valor, de, para):
    if de == 1:
        gramas = valor
    elif de == 2:
        gramas = valor * 1000
    elif de == 3:
        gramas = valor * 453.592
    elif de == 4:
        gramas = valor * 28.3495

    if para == 1:
        return gramas
    elif para == 2:
        return gramas / 1000
    elif para == 3:
        return gramas / 453.592
    elif para == 4:
        return gramas / 28.3495


def pedir_numero(mensagem, opcoes_validas):
    while True:
        try:
            numero = int(input(mensagem))
            if numero not in opcoes_validas:
                print('ERRO: OPÇÃO INVÁLIDA')
                continue
            return numero
        except ValueError:
            print('ERRO: DIGITE UM NÚMERO')

def pedir_valor():
    while True:
        try:
            return float(input('\nDigite o valor a ser convertido: '))
        except ValueError:
            print('ERRO: DIGITE UM NÚMERO VÁLIDO')

def escolher_unidades(nome_categoria, unidades):
    print(f'\nUnidades disponíveis ({nome_categoria}):')
    for numero, nome in unidades.items():
        print(f'{numero}: {nome}')

    opcoes = list(unidades.keys())
    origem = pedir_numero('\nEscolha a unidade de origem: ', opcoes)
    destino = pedir_numero('\nEscolha a unidade de destino: ', opcoes)
    return origem, destino

def executar_conversao(nome_categoria, unidades, funcao_conversao, casas_decimais):
    origem, destino = escolher_unidades(nome_categoria, unidades)
    valor = pedir_valor()
    resultado = funcao_conversao(valor, origem, destino)
    print(f'\n{valor} {unidades[origem]} = {resultado:.{casas_decimais}f} {unidades[destino]}')


def main():
    unidades_distancia = {1: 'metros', 2: 'quilômetros', 3: 'centímetros', 4: 'milímetros'}
    unidades_moeda = {1: 'BRL', 2: 'USD', 3: 'EUR'}
    unidades_tempo = {1: 'segundos', 2: 'minutos', 3: 'horas', 4: 'dias'}
    unidades_temperatura = {1: '°C', 2: '°F', 3: 'K'}
    unidades_massa = {1: 'gramas', 2: 'quilogramas', 3: 'libras', 4: 'onças'}

    conv = pedir_numero(
        '\nDIGITE QUAL A CONVERSÃO\n--------------------------------------------\n'
        '1: Distância\n2: Moeda\n3: Tempo\n4: Temperatura\n5: Massa\n'
        '--------------------------------------------\nRESPOSTA AQUI: ',
        [1, 2, 3, 4, 5]
    )

    if conv == 1:
        executar_conversao('Distância', unidades_distancia, converter_distancia, 4)
    elif conv == 2:
        executar_conversao('Moeda', unidades_moeda, converter_moeda, 2)
    elif conv == 3:
        executar_conversao('Tempo', unidades_tempo, converter_tempo, 4)
    elif conv == 4:
        executar_conversao('Temperatura', unidades_temperatura, converter_temperatura, 2)
    elif conv == 5:
        executar_conversao('Massa', unidades_massa, converter_massa, 4)

    print('\nConversão realizada com sucesso!')

if __name__ == '__main__':
    main()