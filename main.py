# 1) O valor da variável SOMA ao final do processamento pode ser encontrado executando o código:
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(f'a soma é igual a ',SOMA)

print('............................................................................................')

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o
# próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e
# retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci_contains(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

numero = int(input("Informe um número: "))
if fibonacci_contains(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
    
print('............................................................................................')

# 3) Descubra a lógica e complete o próximo elemento:

# Sequência a)
sequence = [1, 3, 5, 7]

# Lógica para o próximo elemento
next_element = sequence[-1] + 2
sequence.append(next_element)

print("Sequência a):", sequence)

# Sequência b)
sequence = [2, 4, 8, 16, 32, 64]

# Lógica para o próximo elemento
next_element = sequence[-1] * 2
sequence.append(next_element)

print("Sequência b):", sequence)

# Sequência c)
sequence = [0, 1, 4, 9, 16, 25, 36]

# Lógica para o próximo elemento
next_element = sequence[-1] + 7
sequence.append(next_element)

print("Sequência c):", sequence)

# Sequência d)
sequence = [4, 16, 36, 64]

# Lógica para o próximo elemento
next_element = sequence[-1] + 20
sequence.append(next_element)

print("Sequência d):", sequence)

# Sequência e)
sequence = [1, 1, 2, 3, 5, 8]

# Lógica para o próximo elemento
next_element = sequence[-1] + sequence[-2]
sequence.append(next_element)

print("Sequência e):", sequence)

# Sequência f)
sequence = [2, 10, 12, 16, 17, 18, 19]

# Lógica para o próximo elemento
next_element = sequence[-1] + 1
sequence.append(next_element)

print("Sequência f):", sequence)

print('............................................................................................')

# 4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente.
# Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.
# Seu objetivo é descobrir qual interruptor controla qual lâmpada.

# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, 
# qual interruptor controla cada lâmpada?

def descobrir_interruptores():
    # Ligar o primeiro interruptor
    print("Ligando o primeiro interruptor...")
    # Simular o comportamento das lâmpadas
    l1, l2, l3 = False, False, False
    l1 = not l1
    print("Verificando as lâmpadas...")

    # Desligar o primeiro interruptor e ligar o segundo interruptor
    print("Desligando o primeiro interruptor e ligando o segundo interruptor...")
    l2 = not l2
    print("Verificando as lâmpadas...")

    # Desligar o segundo interruptor e ligar o terceiro interruptor
    print("Desligando o segundo interruptor e ligando o terceiro interruptor...")
    l3 = not l3
    print("Verificando as lâmpadas...")

    # Determinar qual interruptor controla cada lâmpada
    if l1:
        print("A lâmpada 1 está acesa. O interruptor 1 controla esta lâmpada.")
    else:
        print("A lâmpada 1 está apagada. O interruptor 1 controla esta lâmpada.")

    if l2:
        print("A lâmpada 2 está acesa. O interruptor 2 controla esta lâmpada.")
    else:
        print("A lâmpada 2 está apagada. O interruptor 2 controla esta lâmpada.")

    if l3:
        print("A lâmpada 3 está acesa. O interruptor 3 controla esta lâmpada.")
    else:
        print("A lâmpada 3 está apagada. O interruptor 3 controla esta lâmpada.")

# Chamando a função para descobrir os interruptores
descobrir_interruptores()

print('............................................................................................')

# 5) Escreva um programa que inverta os caracteres de um string.
def inverter_string(string):
    string_invertida = ''
    for caracter in string:
        string_invertida = caracter + string_invertida
    return string_invertida

# Exemplo de uso
string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)

