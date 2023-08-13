# EXERCÍCIO DA AULA PASSADA
# Crie uma função que encontre e retorne o menor e o maior valor da lista,
# e seus índices
## SEM utilizar a função nativa do python (min e max);
## mas agora utilizando a função sort() ou sorted() de listas
lista=[1,5,7,3,-5,100,2]

#lista.sort()  #altera a lista original para sempre

#opção 1: sorted
def maior_menor_sorted(lista):
    lista_ordenada = sorted(lista) #gera uma nova lista ordenada
    #print(lista_ordenada) #[-5, 1, 2, 3, 5, 7, 100]
    maior_valor = lista_ordenada[-1]
    menor_valor = lista_ordenada[0]
    indice_maior = lista.index(maior_valor)
    indice_menor = lista.index(menor_valor)
    return menor_valor,indice_menor,maior_valor,indice_maior

#opção 2: sort()
def maior_menor_sort(lista):
    lista_ordenada = lista.copy()
    lista_ordenada.sort()
    maior = lista_ordenada[-1]
    menor = lista_ordenada[0]
    indice_maior = lista.index(maior)
    indice_menor = lista.index(menor)
    return menor, indice_menor, maior, indice_maior

# print(lista)
# menor_valor,indice_menor,maior_valor,indice_maior = \
#     maior_menor_sort(lista)
# print(maior_valor,indice_maior)
# print(menor_valor,indice_menor)
#
# print()
# print(lista)
# menor_valor,indice_menor,maior_valor,indice_maior = \
#     maior_menor_sorted(lista)
# print(maior_valor,indice_maior)
# print(menor_valor,indice_menor)







#exemplo em aberto:
# criar uma rotina que encontre arquivo da última aula,
# pegue seu número, adicione 1
# e crie um arquivo python com esse novo nome

# import os
# lista_arquivos=os.listdir(r"C:\Users\paulo\PycharmProjects\ComputationalThinking\1TDSPW\1SEM")

#vamos descobrir quantas extensões diferentes tem, e quais são elas
# palavra=""
# lista_para_salvar_ext = []
# for i in lista_arquivos:
#     extensao = i.split(".")[-1] #isolei as extensões
#     #print(extensao)
#
#     ''' este bloco não está sendo utilizado na construção final
#     foi apenas para desenvolver o raciocínio
#     # if extensao != palavra:
#     #     print("Detectada extensão nova:",extensao)
#     #     palavra = extensao
#     '''
#
#     if extensao not in lista_para_salvar_ext:
#         lista_para_salvar_ext.append(extensao)
#         print("Detectada extensão nova:", extensao)
# print("Há {} extensoes de arquvios diferentes".format(len(lista_para_salvar_ext)))

# agora, vamos contar quantas de cada existem
# para fazer com listas, não seria muito eficiente. Para isto, melhor utilizar:
#DICIONÁRIOS

#para construir, utilizamos {}
# sintaxe: {"chave":valor, "chave2":"valor"}
# não trabalhamos com índices, mas sim com chaves
aluno = {"Nome": "Fulano de tal", "RM": 123456}
#print(aluno)
#print(type(aluno))

# print(aluno.keys())
# #print(type(aluno.keys()))
# print(aluno.values())
# #print(type(aluno.values()))
# print(aluno.items())
#print()
#para eu acessar os valores do dicionário, eu não utilizao índices;
# mas sim as chaves (keys)
#print(aluno[0]) #ele vai procurar a chave 0 dentro do dicionário, ao invés de pegar o índice 0
#print(aluno["Nome"])

#a classe keys é interável:
# for key in aluno.keys():
#     print(aluno[key])
#     print(aluno.get(key))

#eu posso alterar e criar valores num dicionário
aluno["Nome"]="Ciclano" #a alteração é irreversível
#print(aluno)

aluno["ano_nascimento"] = 1111 #criei o elemento
print(aluno)
aluno["ano_nascimento"] += 1 #incrementei o valor da chave
print(aluno)

#para saber se um dicionário já possui uma chave
#OBS: o has_key() foi removido no python3!
print("cidade" in aluno.keys())

#vamos utilizar dicionários para contar quantas extensões de cada existem

palavra=""
lista_para_salvar_ext = []
contagem = {}
for i in lista_arquivos:
    extensao = i.split(".")[-1] #isolei as extensões
    ''' este bloco não está sendo utilizado na construção final
    foi apenas para desenvolver o raciocínio
    # if extensao != palavra:
    #     print("Detectada extensão nova:",extensao)
    #     palavra = extensao
    '''

    if extensao not in lista_para_salvar_ext: #caso nao exista
        lista_para_salvar_ext.append(extensao) #add na lista
        contagem[extensao] = 1 # add no dicionário
        print("Detectada extensão nova:", extensao)

    else: #caso exista
        contagem[extensao] += 1

print("Há {} extensoes de arquvios diferentes".format(len(lista_para_salvar_ext)))

print(contagem)

#EXERCÍCIOS:

#1) Crie uma função que receba um número inteiro positivo N como parâmetro
# (e que por padrão seja =1) e retorne um dicionário cujas chaves
# são os números de 0 até N, e os valores, seus quadrados
# ex: N=3, dict={0:0,1:1,2:4,3:9}

#2) Crie uma função que receba um dicionário e some e retorne
# seus valores numéricos
# Caso não exista nenhum, deverá imprimir uma mensagem de erro

#3) Transforme duas listas de tamanhos iguais e um dicionário
# ex: [1,2] e ["um","dois"] viram {1:"um",2:"dois}

#4) faça uma função que extraia recebe um dicionário e
# qualquer número de chaves, e retorne um novo dicionário contendo
# apenas estas chaves
# ex: dict1={"nome": "Fulano","idade": 25,"cidade": "Rio de Janeiro"}
#     chave = "nome"
#    retorno = {"nome":Fulano}

