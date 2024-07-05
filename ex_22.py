dias = ("Domingo","Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sábado")

d = int(input("Digite o número do dia da semana: "))

if 0 < d <= 7:
    print(f"O dia da semana é {dias[d - 1]}")
else: 
    print("VALOR INVALIDO")