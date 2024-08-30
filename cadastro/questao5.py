def inverter_string(s):
    ###Criando a Lista.....
    resultado = []
    
    ###Iterando a string...

    for i in range(len(s) - 1, -1, -1):
        resultado.append(s[i])
    
    ### Convertendo a lista -_-

    return ''.join(resultado)

def main():
    # Input de string
    entrada = input("Digite a string que deseja inverter: ")
    
    string_invertida = inverter_string(entrada)
    
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
