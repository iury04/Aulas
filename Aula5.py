# idade = int(input("Qual é sua idade? "))
# if idade <= 12:
#     print("Você pode brincar! ")
# else:
#     print("Vai embora pra sua casa! ")



# altura = float(input("Qual é a sua altura? "))
# if altura >= 1.60:
#     print("Você pode usar esse aparelho!")
# else:
#     print("Você não pode usar esse aparelho.")



preco_compra = float(input("Qual é o valor da compra? "))
pergunta_cupom = input("Você tem cupom? S/N? ")
if pergunta_cupom == "N": 
    print(f"Preço final: R$ {preco_compra}")
else:
    cupom = "LINDODEMAIS"
    pergunta2_cupom = input("Qual é o cupom? ")
    if pergunta2_cupom != cupom:
        print("Cupom errado.")
        print(f"Preço final: R$ {preco_compra}")
    else:
        valor_do_desconto = preco_compra * (10/100)
        valor_final = (preco_compra - valor_do_desconto)
        print(f"Preço final: {valor_final}")

