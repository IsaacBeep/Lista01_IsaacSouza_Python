#Escreva um programa que pergunte o valor total da conta em seguida pergunte quantos clientes existem, divida a conta pelos clientes e exiba o quanto cada cliente deve pagar seguida da mensagem "Cada cliente deve pagar: " x valor
a = int (input("Qual foi o valor total da conta?: "))
b = int (input("Quantos clientes existem?: "))
c = (a / b)
print("Cada cliente deve pagar: ", c)