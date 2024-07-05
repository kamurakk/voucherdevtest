dias = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")

d = int(input("Digite o número do mês: "))

if 0 < d <= 12:
    print(f"O mês digitado é {dias[d - 1]}")
else: 
    print("VALOR INVALIDO")