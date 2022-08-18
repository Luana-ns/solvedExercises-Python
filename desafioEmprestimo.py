# Desafio número 36 do Curso de Python do Curso em Vídeo.
# Escrever um programa para aprovar um empréstimo bancário para a compra de uma casa.

valor = input ('Digite o valor da casa: ')
salario = input ('Digite o seu salário: ')
anos = input('Digite em quantos anos você quer dividir as parcelas: ')

mensalidade = float(valor)/(float(anos)* 12)

if mensalidade <= (float(salario) * 30/100):
    print (f'Para pagar uma casa de R${round(float(valor), 2)} em {anos} anos a prestação será de R${round(float(mensalidade), 2)}. Empréstimo aprovado!')
else:
    print(f'Para pagar uma casa de R${round(float(valor), 2)} em {anos} anos a prestação será de R${round(float(mensalidade), 2)}. Empréstimo NEGADO!')