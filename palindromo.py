# Dados dois inputs a uma function, determinar se estes são palíndromos.

def palindromo(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        print('Não é um palíndromo.')
        return
    for i, j in enumerate(palavra1):
        if palavra1[i] != palavra2[len(palavra2)-1 -i]:
            print('Não é um palíndromo.') 
            return
    print('É um palíndromo.')




palindromo('amor', 'rmoa')
    