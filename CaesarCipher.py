# Implementar a Cifra de César
# dado uma palavra, rotacione suas letras em 3
# responder o que significa as palavras
# Ydprv dsuhqghu fulswrjudild?
# Ydl sud flpd ghohv Jdor!


# Usando tabela ascii:

mensagem = input('Digite a mensagem: ')
chave = int(input('Digite o valor da cifra: '))
resultado = ''
for i in range(len(mensagem)):
    if (ord(mensagem[i]) < 65 or ord(mensagem[i]) > 122):
        resultado += (mensagem[i])
    else:
        resultado += chr(ord(mensagem[i]) - chave)
print('')


# Sem usar tabela ascii:


alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
cifra = int(input('Digite o valor da cifra:'))  # rotação
mensagem = input("Digite a mensagem: ").upper()
resultado = ''
for i in mensagem:
    pos = alfabeto.find(i)
    new_pos = pos - cifra
    if i in alfabeto:
        resultado += alfabeto[new_pos]
    else:
        resultado += i
print('Resultado: ' + resultado)
