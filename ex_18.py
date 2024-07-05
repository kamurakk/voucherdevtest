n = input("Digite o sexo: [M ou F] ").upper()
alt = float(input("Digite a altura: "))

if n == "M":
    print(f"O peso ideal é de {72.7 * alt - 58}")
elif n == "F":
    print(f"O peso ideal é de {62.1 * alt - 44.7}")
else:
    print("Digite um valor válido")