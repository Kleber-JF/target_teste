# Função para definir a sequencia de fibonacci
def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence


# Função para verificar se o número fornecido pertence à sequência
def is_in_fibonacci(number):
    sequence = fibonacci_sequence(number)
    if number in sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} não pertence à sequência de Fibonacci."


# Número a ser verificado e resultado
number_to_check = int(input("Informe um número: "))
result = is_in_fibonacci(number_to_check)
print(result)
