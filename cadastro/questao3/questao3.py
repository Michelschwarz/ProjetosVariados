import json

def calcular_faturamento(dados):
    ###Filtra os dias com lucro da empresa
    dias_com_faturamento = [valor for valor in dados.values() if valor > 0]
    
    print(f"Dias com faturamento: {dias_com_faturamento}")  # Debug

    if not dias_com_faturamento:
        return None, None, 0  # Caso não haja dias com faturamento
    
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

def main():
    ##### Atualize o caminho do arquivo JSON se necessário
    caminho_arquivo = r'C:\Users\Rudimar\Desktop\cadastro\questao3\faturamento.json'
    
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            print(f"Dados carregados: {dados}")  # Debug
    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return

    menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(dados)

    if menor_faturamento is not None:
        print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
        print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
    else:
        print("Não há dias com faturamento para calcular.")

if __name__ == "__main__":
    main()
