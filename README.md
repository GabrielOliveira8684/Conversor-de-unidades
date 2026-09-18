# Conversor de Unidades (Python)

Um conversor de unidades interativo desenvolvido em Python para praticar modularização de código, tratamento de exceções e estruturas de decisão. O projeto evoluiu de um script único e repetitivo para uma versão mais organizada, reduzindo duplicação de código e deixando a validação de entrada mais robusta.

## O que ele faz?

Permite ao usuário escolher entre 5 tipos diferentes de conversão diretamente pelo terminal:

* **Distância**: Metro, Quilômetro, Centímetro, Milímetro
* **Moeda**: Real (BRL), Dólar (USD), Euro (EUR)
* **Tempo**: Segundos, Minutos, Horas, Dias
* **Temperatura**: Celsius, Fahrenheit, Kelvin
* **Massa**: Gramas, Quilogramas, Libras, Onças

Depois é só escolher a unidade de origem, a de destino e o valor — a conversão sai na hora.

## Como rodar

Se você tiver o Python instalado na sua máquina, siga os passos abaixo:

1. Clone o repositório:
```bash
git clone https://github.com/GabrielOliveira8684/Conversor-de-unidades.git
```

2. Execute o arquivo:
```bash
python conversor.py
```

3. Siga as instruções na tela: escolha o tipo de conversão, as unidades e o valor.

## O que eu pratiquei e aprendi nesse projeto

Essa atualização foi importante pra eliminar repetição de código e deixar o programa mais resistente a erros de entrada:

* **Modularização com Funções:** Refatorei a parte repetitiva do código em funções genéricas e reutilizáveis (`pedir_numero`, `pedir_valor`, `escolher_unidades`, `executar_conversao`), que funcionam pra qualquer categoria de conversão, evitando duplicar a mesma lógica de menu e validação 5 vezes.
* **Tratamento de Exceções:** Troquei a validação manual de strings (`while uni not in [...]`) por `try/except`, capturando `ValueError` pra impedir que o programa quebre se o usuário digitar uma letra no lugar de um número.
* **Funções com Responsabilidade Única:** Separei claramente as funções de cálculo (a conversão em si) das funções de interação com o usuário (pedir dados, exibir opções, executar o fluxo), facilitando manutenção e leitura do código.
* **Uso de `main()`:** Organizei o fluxo principal do programa dentro de uma função `main()`, protegida por `if __name__ == '__main__':`, seguindo uma boa prática comum em projetos Python.
* **Dicionários:** Continuei usando dicionários pra armazenar taxas de câmbio e nomes das unidades, agora passados como parâmetro pras funções genéricas em vez de ficarem espalhados pelo código.
* **Formatação de Saída:** Mantive `.4f` e `.2f` pra deixar as respostas mais legíveis, agora com o número de casas decimais definido dinamicamente por categoria de conversão.

Valeu!