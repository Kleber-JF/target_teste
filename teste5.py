def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ""
    # Itera sobre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida


# Entrada da string no terminal
string_original = input("Informe uma string para inverter: ")
string_reversa = inverter_string(string_original)
# Saída do resultado
print(f"String original: {string_original}")
print(f"String invertida: {string_reversa}")
