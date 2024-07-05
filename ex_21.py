n1 = int(input("Digite a nota de trabalho: "))
n2 = int(input("Digite a nota da avaliação: "))
n3 = int(input("Digite a nota do exame final: "))


if 0 <= n1 <= 10: 
    if 0 <= n2 <= 10:
        if 0 <= n3 <= 10:
            fnl = (n1 * 0.2 + n2 * 0.3 + n3 * 0.5)
            print(f"A média destas notas é {fnl:.1f} pontos")
            if fnl <= 3:
                print("Está REPROVADO")
            elif fnl <= 5.9:
                print("Está de recuperação")
            else:
                print("APROVADO")
        else:
            print("Nota 3 é inválida")
    else:
        print("Nota 2 é inválida")
else:
    print(f"Nota 1 é inválida")