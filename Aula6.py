# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# if num1 > num2:
#     print(f"O númeor {num1} é maior. ")
# elif num1 < num2:
#     print(f"O número {num2} é maior. ")
# else:
#     print("Os números são iguais. ")




# nota = float(input("Qual foi sua média? "))
# if nota >= 7:
#     print("Resultado: Aprovado. ")
# elif nota >= 5:
#     print("Resultado: Recuperação. ")
# else: 
#     print("Resultado: Reprovado. ")



peso = float(input("Qual é seu peso? "))
altura = float(input("Qual é sua altura? "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do peso. ")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade. ")