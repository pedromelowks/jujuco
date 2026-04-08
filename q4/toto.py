def intercalar_vetores():
    # 1. Leitura do primeiro vetor
    n1 = int(input("Tamanho do primeiro vetor: "))
    vetor1 = []
    print(f"Digite os {n1} elementos (em ordem crescente):")
    for _ in range(n1):
        vetor1.append(int(input()))

    # 2. Leitura do segundo vetor
    n2 = int(input("\nTamanho do segundo vetor: "))
    vetor2 = []
    print(f"Digite os {n2} elementos (em ordem crescente):")
    for _ in range(n2):
        vetor2.append(int(input()))

    # 3. Geração do terceiro vetor ordenado (Lógica de Intercalação)
    vetor3 = []
    i = j = 0

    # Percorre ambos os vetores comparando os elementos
    while i < n1 and j < n2:
        if vetor1[i] <= vetor2[j]:
            vetor3.append(vetor1[i])
            i += 1
        else:
            vetor3.append(vetor2[j])
            j += 1

    # Se sobrarem elementos no vetor1, adiciona ao final
    while i < n1:
        vetor3.append(vetor1[i])
        i += 1

    # Se sobrarem elementos no vetor2, adiciona ao final
    while j < n2:
        vetor3.append(vetor2[j])
        j += 1

    # 4. Exibição do resultado
    print("\n" + "="*30)
    print(f"Vetor 1: {vetor1}")
    print(f"Vetor 2: {vetor2}")
    print(f"Vetor 3 (Intercalado): {vetor3}")
    print("="*30)

if __name__ == "__main__":
    intercalar_vetores()