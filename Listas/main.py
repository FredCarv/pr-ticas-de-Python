#LISTAS
#criando uma lista vazia:
lista1 = []
#criando uma lista com itens:
lista2 = [1, 5, 9]

#adicionando um elemento à lista
# append (sempre ao final dalista)
print(lista1)
lista1.append(1)
print(lista1)
lista1.append(5)
lista1.append("string")
lista1.append(lista2)
print(lista1)
print("----------")
#acesso itens da minha lista através do índice
#lembrando que o índice cimeça no 0
print(lista1[1])

#alterando itens da lista:
#localizar pelo índice e alterar
lista1[1] = 9
print("Lista 1 após alteração:", lista1)

#tamanho da lista = len(lista)
print("a lista 1 tem {} itens.".format(len(lista1)))

#pegando o último item utilizando o len
#tenho que descontar
tamanho_da_lista = len(lista1)
indice_do_ultimo_item = tamanho_da_lista-1
print(lista1[indice_do_ultimo_item])

#acessando diretamente o último
print(lista1[-1])

#acessar partes de lista (slices)
#o ponto de partida e de chegada funciona igual no range do for
print(lista1[0:2])

#se eu tiver apenas valores numéricos, posso utilizar o sum(lista) para somar todos os valores
lista_numeros = [5, 7, 94, 5, .85, 7956]
print(sum(lista_numeros))

#se eu quiser a média dos numeros da lista:
media_da_lista = sum(lista_numeros)/len(lista_numeros)
print(media_da_lista)

#retirando itens da lista: temos 2 opções

## .pop() , onde escolhemos o ÍNDICE
### o .pop() RETORNA o valor retirado

lista = [1, 4, 9, 7, 9]
print("lista original", lista)
print(lista.pop(1))
print("lista após pop(1): ", lista)
### .remove() , onde escolhemos o VALOR (a primeira ocorrência)
###o .remove() NÃO retorna valor
print(lista.remove(9))
print("lista após remove(9): ", lista)

#removendo todas as ocorrências de um valor na lista
#vamos remover todos os '5'
lista = [1,5,7,5,5,9,6,87,4,5]

lista_reserva = lista.copy()

for i in range(len(lista)):
    print("interação: ",i)
    print("avaliação atual: ", lista[i])
    if lista[i] == 5:
        lista_reserva.remove(5)
    print("lista original após remoção: ",lista)
    print("lista reserva após remoção: ", lista_reserva)

#FAZER COM WHILE