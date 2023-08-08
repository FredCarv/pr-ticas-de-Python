lista =[1,5,7,5,5,9,6,87,4,5]


def encontra_extremos(lista):
    maior = float("-inf")
    menor = float('inf')
    for i in lista:
        if i> maior:
            maior = i

        if i < menor:
            menor = i

    indice_maior = lista.index(maior)
    indice_menor = lista.index(menor)

    return maior,menor,indice_menor,indice_maior

maior,menor,indice_menor,indice_maior = encontra_extremos(lista)

# print(f"O maior número é {maior}")
# print(f"O menor número é {menor}")
# print(f"o maior número da lista está na posição {indice_maior}")
# print(f"o menor número da lista está na posição {indice_menor}")


# TUPLAS
lista = [1,5,7,5,5,9,6,87,4,5]
tupla = (1,5,7,5,5,9,6,87,4,5)

lista[0] = 0
# print(lista)
#a tupla [0]=0  #da erro pq tupla não pode ser alterada
#a tupla possui as mesmas funções da lista que não a alterem
# print(len(tupla))
# print(tupla[0])

#posso transformar uma lista em tupla
tupla2 = tuple(lista)
# tupla2[0] = 7  #retorna erro pq foi transformada em tupla

#para criar uma tupla, eu preciso de uma vpirgula
tupla_1 = (5) # não é tupla
tupla_2 = (5,)
tupla_3 = 5,2
tupla_4 = tupla_2 + tupla_3

# print(type(tupla_1))
# print(type(tupla_2))
# print(type(tupla_3))
# print()
# print(tupla_4)


#STRINGS[

string = "palavra"
print(len(string))
print(string[0])
print(sorted(string))
print(string)

sorted_string = sorted(string)

string_final = "" #equivale a lista_final = []
for i in sorted_string:
    string_final += i

print(string_final)
print("".join(i for i in sorted_string if i != "a"))

