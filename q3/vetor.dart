def contar_frequencia():
    # 1. Lê o valor de N (tamanho do conjunto)
    try:
        n = int(input("Digite a quantidade de números (N): "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        return

    vetor = []
    
    # 2. Lê os elementos do conjunto
    print(f"Digite os {n} números:")
    for i in range(n):
        num = int(input(f"Elemento {i+1}: "))
        vetor.append(num)

    # 3. Usa um dicionário para contar as repetições
    # Chave = número, Valor = contador
    repeticoes = {}

    for numero in vetor:
        if numero in repeticoes:
            repeticoes[numero] += 1
        else:
            repeticoes[numero] = 1

    # 4. Imprime o resultado conforme o exemplo da imagem
    print("\nResultado:")
    for numero, quantidade in repeticoes.items():
        print(f"{numero} – {quantidade}")

if __name__ == "__main__":
    contar_frequencia() 