num = int(input("Digite um número: "))
invertido = 0

while num > 0:
    # Pega o último dígito
    digito = num % 10
    # Adiciona ao novo número deslocando a casa decimal
    invertido = (invertido * 10) + digito
    # Remove o último dígito do número original
    num = num // 10

print(f"Impressão: {invertido}")