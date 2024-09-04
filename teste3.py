import json


# Função para calcular o menor, maior e dias com faturamento acima da média
def analyze_faturamento(data):
    # Filtrando dias com faturamento maior que 0
    valid_faturamento = [entry['valor']
                         for entry in data if entry['valor'] > 0]

    # Calculando menor e maior faturamento
    menor_faturamento = min(valid_faturamento)
    maior_faturamento = max(valid_faturamento)

    # Calculando média mensal
    media_mensal = sum(valid_faturamento) / len(valid_faturamento)

    # Contando dias com faturamento acima da média
    dias_acima_da_media = sum(1 for valor in valid_faturamento
                              if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media


# Leitura do arquivo e saida dos resultados.
def main():
    with open('dados.json') as file:
        data = json.load(file)
    menor, maior, dias_acima = analyze_faturamento(data)

    print(f"Menor valor de faturamento: {menor}")
    print(f"Maior valor de faturamento: {maior}")
    print(f"Número de dias com faturamento acima da média: {dias_acima}")


# Executa o programa
if __name__ == "__main__":
    main()
