# Partes de uma URL (Uniform Resource Locator):
#

# Esquema, Domínio, Porta, Caminho e Query string.

# 1. **Esquema (Scheme)**: Indica o protocolo de comunicação.

#   Os esquemas mais comuns em sistemas web sÃ£o o "http" e o "https".

# O HTTP (Hypertext Transfer Protocol) Ã© para transferir informaÃ§Ãµes entre um cliente e um servidor.

# Ele permite que os clientes solicitem recursos (pÃ¡ginas da web, imagens, JSON, dados, etc)
# e os servidores respondam fornecendo esses recursos.

# Opera no modelo de solicitaÃ§Ã£o-resposta (request-response),
# onde o **cliente faz requests** para URLs e o **servidor responde (responses)** com os dados solicitados.

# As mensagens HTTP incluem mÃ©todos, como GET para buscar recursos e POST para enviar dados,
# alÃ©m de cÃ³digos de status, como 200 para indicar sucesso ou 404 para indicar que o recurso nÃ£o foi encontrado.

# O HTTPS Ã© a versÃ£o "segura" do HTTP, pois utiliza criptografia para que as informaÃ§Ãµes sejam acessíveis
# apenas para o cliente e o servidor.


# 2. **Domínio (Host)**: Indica o endereÃ§o do servidor onde o recurso estÃ¡ localizado.
# Pode ser um domÃ­nio como https://www.google.com ou um endereÃ§o de IP 3https://142.250.219.4:44 (Google)


# 3. **Porta (Port)**: Ã© opcional e indica o nÃºmero da porta de um servidor a ser usado para acessÃ¡-lo.
# Se nÃ£o for especificada, utiliza-se a porta padrÃ£o para o esquema
# como por exemplo, 80 para HTTP e 443 para HTTPS.

# No exemplo anterior: https://www.google.com:443 ou https://142.250.219.4:443
# (note o :443 no final)


# 4. **Caminho (Path)**: (opcional) Especifica o caminho para o recurso no servidor.
# Pode incluir diretÃ³rios e subdiretÃ³rios.
# Exemplos:
# https://www.google.com/imghp  => Google imagens
# https://www.google.com/search  => Google search


# 5. **Query String**: (opcional) ContÃ©m os parÃ¢metros de consulta para o servidor.
# Ã‰ precedida por um ponto de interrogaÃ§Ã£o "?" e pode conter mÃºltiplos pares chave-valor separados por "&".

#    Exemplo: https://www.google.com/search?q=fiap


# Exemplo com a PokÃ©API
# Site com documentaÃ§Ã£o: https://pokeapi.co/docs/v2
# Acessando uma informaÃ§Ãµes de uma berry:  https://pokeapi.co/api/v2/berry/{id or name}/
# Exemplo: https://pokeapi.co/api/v2/berry/1/ ou https://pokeapi.co/api/v2/berry/cheri/


# Acessando uma API com Python requests:

# primeiramente, temos que instalar o pacote requests
# Digite em seu terminal (fora do python): pip install requests

# em seguida, em um arquivo .py:
# importe o pacote
import requests
import pprint  # uma forma de imprimir "bonito" (pretty)

# print(4 * "\n")
# print(50 * "=")
# print(10 * " ", "Trabalhando com a pokÃ©API")
# print(50 * "=")
# print()
# # envie uma request
# url = "https://pokeapi.co/api/v2/berry/1/"
# response = requests.get(url)
# # trate a resposta de sua requisiÃ§Ã£o:
# if response.status_code == 200:
#     # lista de cÃ³digos de estado: https://pt.wikipedia.org/wiki/Lista_de_c%C3%B3digos_de_estado_HTTP
#     data = response.json()  # Converte a resposta JSON em um dicionÃ¡rio Python
#     # FaÃ§a algo com os dados, como exibir, processar ou armazenar
#     pprint.pprint(data)
# else:
#     print("Falha na solicitaÃ§Ã£o. CÃ³digo de status:", response.status_code)
#
#
#
# # MÃ©todos GET, POST, PATCH e DELETE

# POST -> CREATE
# GET - > READ
# PATCH / PUT -> UPDATE
# DELETE -> DELETE
#
# nestes exemplos, utilizaremos a API jsonplaceholder

# print(4 * "\n")
# print(50 * "=")
# print(10 * " ", "Trabalhando com a API jsonplaceholder")
# print(50 * "=")
# print()

# # GET:
# #    - Ã‰ uma operaÃ§Ã£o de leitura, solicitando dados de um recurso especÃ­fico do servidor.
# #    - Os parÃ¢metros sÃ£o anexados Ã  URL e **sÃ£o visÃ­veis**, transmitidos de forma legÃ­vel na URL.
# #    - NÃ£o modifica os dados no servidor.
# #    - Corresponde a operaÃ§Ã£o READ do CRUD.
# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)
#
# print()
# print(50 * "=")
# print(10 * " ", "Trabalhando com GET na API jsonplaceholder")
# print(50 * "=")
#
# if response.status_code == 200:
#     data = response.json()
#     pprint.pprint(data)
# else:
#     print("Falha na solicitaÃ§Ã£o. CÃ³digo de status:", response.status_code)

# POST:
#    - Ã‰ uma operaÃ§Ã£o de envio de dados dados ao servidor e por isso utilizada para criar novos recurso.
#          Exemplos: envios de formulÃ¡rios web, envios de dados para APIs, etc.
#    - Os dados sÃ£o enviados no corpo (body) da solicitaÃ§Ã£o e nÃ£o na URL, o que os torna menos visÃ­veis.
#    - Corresponde a operaÃ§Ã£o CREATE do CRUD.
# print()
# print(50 * "=")
# print(10 * " ", "Trabalhando com POST na API jsonplaceholder")
# print(50 * "=")
#
# dados_post = {
#     "title": "foo",
#     "body": "bar",
#     "userId": 1,
# }
# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.post(url=url, data=dados_post)
#
# if response.status_code == 201:
#     data = response.json()
#     pprint.pprint(data)
# else:
#     print("Falha na solicitaÃ§Ã£o. CÃ³digo de status:", response.status_code)

# PATCH:
#    - Ã‰ usado para atualizar um recurso JÃ existente no servidor.
#          Exemplos: alteraÃ§Ã£o de informaÃ§Ãµes cadastrais, configuraÃ§Ãµes, etc.
#    - Assim como no POST, Os dados tambÃ©m sÃ£o enviados no body da requisiÃ§Ã£o, neste caso apenas com os campos a serem alterados.
#    - Corresponde a operaÃ§Ã£o UPDATE do CRUD.
# print()
# print(50 * "=")
# print(10 * " ", "Trabalhando com PATCH na API jsonplaceholder")
# print(50 * "=")
#
# dados_patch = {
#     "id": 1,
#     "title": "bar",  # era "foo"
#     "body": "foo",  # era "bar"
#     "userId": 1,
# }
# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.patch(url, dados_patch)
# if response.status_code == 200:
#     data = response.json()
#     pprint.pprint(data)
# else:
#     print("Falha na solicitaÃ§Ã£o. CÃ³digo de status:", response.status_code)
#
# DELETE:
#    - Solicita a remoÃ§Ã£o de um recurso JÃ existente no servidor.
#          Exemplos: remoÃ§Ã£o de um item do catÃ¡logo, remoÃ§Ã£o de um cadastro, etc.
#    - Geralmente nÃ£o requer dados na solicitaÃ§Ã£o, pois a identificaÃ§Ã£o do recurso pode ser feita pela URL.
#    - Corresponde a operaÃ§Ã£o DELETE do CRUD.
#    Curiosidade: muitas aplicaÃ§Ãµes implementam o soft-delete, que trata-se de nÃ£o apagar um registro,
#                 mas marcÃ¡-lo como "inativo" no banco de dados.

# print()
# print(50 * "=")
# print(10 * " ", "Trabalhando com DELETE na API jsonplaceholder")
# print(50 * "=")
#
# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.delete(url=url)
# if response.status_code == 200:
#     print("Deletado com sucesso")
# else:
#     print("Falha na solicitaÃ§Ã£o. CÃ³digo de status:", response.status_code)

# As tratativas de dados e conexÃµes utilizam clÃ¡usulas try/except para aumentar a "resiliÃªncia" do cÃ³digo.
# ExercÃ­cio: reescrever o cÃ³digo acima utilizando try/except
# referÃªncia: https://requests.readthedocs.io/en/latest/_modules/requests/exceptions/



# Exercício 1: filtrar posts dado um userId na API jsonplaceholder
#        ReferÃªncia: https://jsonplaceholder.typicode.com/guide/


# Exercício 2: Criar módulos e/ou funções para lidar com as requisiÃ§Ãµes para a API jsonplaceholder
#            DeverÃ¡ utilizar a biblioteca python requests, tratativas de exceÃ§Ãµes e
#            validaÃ§Ãµes de cÃ³digos de retorno.