# Implementar a Cifra de Vigenère. 
# Dado uma palavra e uma chave, rotacione as letras e retorne.
# Responder o que significa os textos(rot 13)
# Ibpr + Pbzhavqnqr = CbqPbqne
# Yrzoerz-fr qn ncerfragnpnb qr svany qr pvpyb frznan dhr irz!

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
chave = int(input('Digite o valor da cifra: '))  # rotação
mensagem = input("Digite a mensagem: ").upper()
resultado = ''
for i in mensagem:
    pos = alfabeto.find(i)
    new_pos = (pos - chave) % 26
    if i in alfabeto:
        resultado += alfabeto[new_pos]
    else:
        resultado += i
print('Resultado: ' + resultado)
