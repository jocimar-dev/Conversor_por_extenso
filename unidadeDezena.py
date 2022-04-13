class Unidade_Dezena:
    def valores(x, digitos, dicionario_numerico):
        if x == 1:
            for k, v in dicionario_numerico['unidade'].items():
                if int[digitos] == v:
                    print('_' * 10)
                    print(k)
                    print('_' * 10)