#def imprimir_dados(nome, idade=16):
#    print("nome: {}, idade: {}".format(nome, idade))




#imprimir_dados('André')

def somar_numeros(n1, n2):
    return n1 + n2

resultado = somar_numeros(10, 20)
#print(resultado)

def titulos_copa_mundo(pais, *args):
    print('O país {}'.format(pais))
    print('Ganhou a copa do mundo nos anos: ')
    for titulo in args:
        print(titulo)

titulos_copa_mundo('Brasil', '1994', '2002')

