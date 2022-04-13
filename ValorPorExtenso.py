from centenas import Centenas
from dicionarioNumerico import Dicionario_Numerico
from unidadeDezena import Unidade_Dezena

dic_numeros =  Dicionario_Numerico.dic_numerico_valores

valor = input('Digite um numero entre 1 e 999')
while valor != 1000 or valor != 'sair':
    if valor.isnumeric():
        valor = valor.lstrip('0')
        tamanho_valor = len(valor)
    else:
        break
    Unidade_Dezena.valores(tamanho_valor, valor, dic_numeros)
    Centenas.valores(tamanho_valor, valor, dic_numeros)

    valor = input('Digite um numero entre 1 e 999')



