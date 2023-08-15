#1) Crie uma função que receba um número inteiro positivo N como parâmetro
# (e que por padrão seja =1) e retorne um dicionário cujas chaves
# são os números de 0 até N, e os valores, seus quadrados
# ex: N=3, dict={0:0,1:1,2:4,3:9}
'''
#dict = {n:n**2}
def n_quadrado(N=1):
    # dicio = {}
    # for n in range (N+1):
    #     dicio[n] = n**2 #adicionando chave e valor ao dicionário

    dicio = {n:n**2 for n in range(N+1)} #a mesma coisa do loop a cima
    return dicio
dicio_ex_1 = n_quadrado()
print(dicio_ex_1)
'''



#2) Crie uma função que receba um dicionário e some e retorne
# seus valores numéricos
# Caso não exista nenhum, deverá imprimir uma mensagem de erro
'''
def soma_numeros(dicio):
    resposta = 0
    validador = True
    for valor in dicio.values():
        if type(valor) == int or type(valor) == float:
            resposta += valor
            validador = False

    if validador:
        return "Erro! Não possui valores numéricos"
    else:
        return resposta

print(soma_numeros(dicio_ex_1))
print(soma_numeros({0:"0"}))
'''
#3) Transforme duas listas de tamanhos iguais e um dicionário
# ex: [cor,tampa] e ["preta","branca"] viram {cor:"preta",tampa:"branca"}
'''
lista1 = ["cor", "tampa"]
lista2 = ["preta", "branca"]
dicio = {}
for i in range(len(lista1)):
    chave = lista1[i]
    valor = lista2[i]
    dicio[chave] = [valor]
    
    ########## OU ###########
    
    #dicio[lista1[i]] = lista2[i]
    
dicio2 = dict(zip(lista1, lista2)) ##equivale ao for acima
print(dicio)
'''

#4) faça uma função que extraia recebe um dicionário e
# qualquer número de chaves, e retorne um novo dicionário contendo
# apenas estas chaves
#     chave = "nome"
#    retorno = {"nome":Fulano}

dict1={"nome": "Fulano","idade": 25,"cidade": "Rio de Janeiro"}
#chave = "nome"
#retorno = {"nome":Fulano}

dicio = {chave:valor for chave,valor in dict1.items() if chave == "nome"}

print(dicio)
