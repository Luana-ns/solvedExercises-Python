# Desafio 043 do Curso em Vídeo.
# Calcular o Índice de Massa Corporal e classificar a situação na qual a pessoa se encontra.

weight = input ('Digite seu peso atual: ')
height = input ('Digite o a sua altura: ')

imc = float(weight)/float(height)**2

if imc < 18.5:
    print ('Está abaixo do peso.' )
elif imc >= 18.5 and imc < 25:
    print ('Peso ideal.')
elif imc >= 25 and imc < 30:
    print('Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbita.')



