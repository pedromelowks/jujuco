def sistema_universidade():
    professores = []
    valor_hora = 12.30

    while True:
        print("\n" + "="*30)
        print("      MENU PRINCIPAL")
        print("="*30)
        print("1. Adicionar Professor")
        print("2. Deletar Professor")
        print("3. Listar e Ver Médias")
        print("4. Sair")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("\nCódigo: ")
            nome = input("Nome: ")
            sexo = input("Sexo (M/F): ").strip().upper()
            
            # Validação simples de sexo para não quebrar a média depois
            if sexo not in ["M", "F"]:
                print("❌ Erro: Sexo deve ser M ou F. Cadastro cancelado.")
                continue
                
            try:
                horas = float(input("Horas de aula: "))
                bruto = horas * valor_hora
                desconto = 0.10 if sexo == "M" else 0.05
                liquido = bruto * (1 - desconto)

                professores.append({
                    "codigo": codigo,
                    "nome": nome,
                    "sexo": sexo,
                    "liquido": liquido,
                    "bruto": bruto
                })
                print(f"✅ {nome} adicionado!")
            except ValueError:
                print("❌ Erro: Digite um número válido para as horas.")

        elif opcao == "2":
            cod_busca = input("Digite o código para deletar: ")
            original = len(professores)
            professores = [p for p in professores if p['codigo'] != cod_busca]
            if len(professores) < original:
                print("🗑️ Removido com sucesso.")
            else:
                print("⚠️ Código não encontrado.")

        elif opcao == "3":
            if not professores:
                print("\n📭 Lista vazia. Adicione professores primeiro.")
                continue

            # Variáveis para a média
            soma_m = soma_f = 0
            qtd_m = qtd_f = 0

            print("\n--- LISTAGEM ---")
            for p in professores:
                print(f"Cód: {p['codigo']} | Nome: {p['nome']} | Líquido: R$ {p['liquido']:.2f}")
                
                if p['sexo'] == "M":
                    soma_m += p['liquido']
                    qtd_m += 1
                elif p['sexo'] == "F":
                    soma_f += p['liquido']
                    qtd_f += 1

            print("-" * 30)
            # Cálculo seguro das médias (evita divisão por zero)
            media_m = soma_m / qtd_m if qtd_m > 0 else 0
            media_f = soma_f / qtd_f if qtd_f > 0 else 0

            print(f"Média Masculina: R$ {media_m:.2f}")
            print(f"Média Feminina:  R$ {media_f:.2f}")

        elif opcao == "4":
            break

if __name__ == "__main__":
    sistema_universidade()