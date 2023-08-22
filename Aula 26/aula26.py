#EXERCÍCIO:
# vamos criar uma função que adiciona um dicionário
# contendo o cadastro do aluno à lista de alunos
# porém, de forma que o RM seja único por aluno
#{"Nome": "Fulano", "Curso": "TDS", "RM":123}
# assumindo que não há remoção de alunos

lista_de_alunos = []
# como não há remoção, podemos utilizar o tamanho da lista
# como ID único

def adiciona_aluno(nome, curso, lista_de_alunos):

    dicio_aluno = {
        "Nome": nome,
        "Curso": curso,
        "RM": len(lista_de_alunos)+1
    }
    lista_de_alunos.append(dicio_aluno)

#print(lista_de_alunos)
adiciona_aluno("Fulano","TDS",lista_de_alunos) #eu não atribuo a uma lista nova, pois minha função não tem retorno
adiciona_aluno("Fulano","TDS",lista_de_alunos)
adiciona_aluno("Fulano","TDS",lista_de_alunos)
#print(lista_de_alunos)
#print(len(lista_de_alunos))


#Agora, a partir do exercício anterior, faça com que a função que receba a lista de alunos
# e assinale o aluno a uma Turma, da seguinte forma:
# Caso seu RM seja par, adicioná-lo à turma W
# Caso contrário, adicionar à turma X
# Lembrando que o código da turma começa com 1 e é seguido do código do curso.
# Após esta designação, remova do dicionário a informação do curso
# (pois já estará contido na turma) e adicione este dicionário a uma nova lista
# ex: {"Nome": "Fulano", "RM":123, "Turma": "1TDSX"}

lista_de_turmas = []
def adiciona_turma(lista_de_alunos):
    for aluno in lista_de_alunos:
        # {"Nome": "Fulano", "Curso": "TDS", "RM":123}
        curso = aluno["Curso"]
        nome = aluno["Nome"]
        rm = aluno["RM"]
        if rm % 2 == 0: #turma W
            turma = "1"+curso+"W"
        else: #turma X
            turma = "1"+curso+"X"

        dicio_turma = {
            "Nome": nome,
            "RM": rm,
            "Turma": turma
        }
        lista_de_turmas.append(dicio_turma)
#print()
adiciona_turma(lista_de_alunos)
#print(lista_de_turmas)
#print(len(lista_de_turmas))


# MANIPULAÇÃO DE TEXTOS:
#utilizamos a função open (abrir)
#temos 3 modos principais de abrir um arquivo:
## r = read (ler) -> apenas para arquivos existentes
## w = write (escrever) -> sempre SOBRESCREVE ; consigo CRIAR arquivos
## a = append (adicionar) -> adiciona ao FINAL do arquivo ; também cria arquivos

#ao abrir um arquivo, temos que fechar ao final da manipulação
#arquivo = open("teste2.txt","w")
...
#arquivo.close()

#temos uma outra opção de abrir e fechar: with (com)
#with open("teste.txt","r") as arquivo:
    #estou manipulando este arquivo
#    ...

#não estou mais manipulando o arquivo

#####################
#vamo ESCREVER no arquivo
#lembrando que, quando queremos pular linhas numa string: \n

#vamos supor que queremos salvar a lista de alunos em um arquivo
# cada um em uma linha
# print(lista_de_alunos)
# with open("lista_de_alunos.txt","w") as arquivo:
#     #arquivo.write(str(lista_de_alunos)) #escrevo apenas 1 item (uma linha) de uma vez só
#
#     #é diferente de :
#     #for item in lista_de_alunos:
#     #    arquivo.write(str(item)) #escreve todos os itens um do lado do outro
#
#     #é diferente de :
#     for item in lista_de_alunos:
#         arquivo.write(str(item)) #não importa quantas linhas diferentes eu escreva no python
#         #arquivo.write(str(item)) #ele só vai salvar uma quebra de linha quando eu
#         arquivo.write("\n")      #escrever explicitamente

for i in range(5):
    print(i)
print()
print("Ola!\nBoa noite")
#####################
#vamo LER do arquivo
#vamos supor que queremos ler a lista de alunos de um arquivo
with open("lista_de_alunos.txt","r") as arquivo:
    leitura = arquivo.readlines() #retorna uma lista com o conteúdo do arquivo em formato de string
    for i in leitura:
        print(i)
        print(type(i))
        #print(i.keys()) #vai dar erro pois não é mais um dicionário
        #dicio_i = dict(i) #deu erro
        #print(dicio_i)

#EXERCÍCIO:
# como vocês manipulariam uma string contendo um dicionário para formar um dicionário?

# ex: "{'Nome': 'Fulano', 'Curso': 'TDS', 'RM': 1}"

ex = "{'Nome': 'Fulano', 'Curso': 'TDS', 'RM': 1}"

quebra = ex.split(",")
for i in quebra:
    if i == quebra[0]: #isolei a abertura da chave
        #opção1:
        print(i.split("{")[-1])
        #opção 2:
        print(i[1:])

    elif i == quebra[-1]: #isolei o fechamento da chave
        #opção 1:
        print(i.split("}")[0].split(":"))
        #opção 2:
        print(i[:-1])
    else:
        print(i.split(":"))
