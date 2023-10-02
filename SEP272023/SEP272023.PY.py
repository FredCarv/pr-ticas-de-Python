# revisÃ£o dos conceitos de API:
# - partes de uma URL:
#   1. protocolo:
#         http e https ("seguro" por ser criptografada)
#   2. domínio: "endereÃ§o" num formato de "nome"
#   3. porta:
#        - 80  -> http
#        - 443 -> https
#   4. caminho (path)
#   5. query string:
#       parÃ¢metros
# URL   protocolo://dominio:porta/caminho?query_string


# POST          ~~  CREATE
#               {
#                   'titulo': 'texto titulo',
#                   'corpo da postagem': 'texto do blog'
#               }
# GET           ~~  READ
# PUT / PATCH   ~~  UPDATE
#     PATCH  --> envio o que deve ser modificado
#            alterar o atributo titulo
#                  {title: "texto do novo tÃ­tulo"}
#     PUT    --> envio toda a informaÃ§Ã£o (o que deve ser alterado + o que nÃ£o deve)
#               espÃ©cie de POST + PATCH
#            se o id=xyz existe, reescreve
#            caso contrÃ¡rio, cria um novo
#               {
#                   'titulo': 'texto do novo tÃ­tulo',
#                   'corpo da postagem': 'texto do blog' (antigo texto)
#               }
# DELETE        ~~  DELETE

# open('arquivo', 'w')
# open('arquivo', 'r+')
# open('arquivo', 'a')

#  o url a seguir é um método GET, POST, PUT, PATCH, DELETE, etc?
#  justifique
#  https://jsonplaceholder.typicode.com/posts?userId=1


import requests

# # ExercÃ­cio 1: filtrar posts dado um userId na API jsonplaceholder
# #  Quantos posts o User com ID = 1 possui?
# #        ReferÃªncia: https://jsonplaceholder.typicode.com/guide/
# user_id = 1
# base_url = "https://jsonplaceholder.typicode.com"
# url_posts_por_user = f"{base_url}/posts?userId={user_id}"
#
# response = requests.get(url_posts_por_user)
# if response.status_code == 200:  # significa OK!
#     data = response.json()
#     print(f"O user de id {user_id} possui {len(data)} posts")
# else:
#     print("Falha na requisiÃ§Ã£o")

# # ExercÃ­cio 1 - parte 2
## Para todos os users, construa um dicionÃ¡rio de dicionÃ¡rios em que as chaves sejam (username, id) e as sub-chaves:
##  - num_posts: a contagem de posts de cada usuÃ¡rio
##  - num_comments: o total de comentÃ¡rios de todos os posts
##  - posts: lista de dicionÃ¡rios contendo title e body
##  - comments: lista de dicionÃ¡rios contendo name, email e body do comentÃ¡rio.

import pprint

base_url = "https://jsonplaceholder.typicode.com"


class ErroListaPosts(Exception):
    ...


class ErroListaPostComments(Exception):
    ...


def lista_posts_por_user(user_id):
    url_posts_por_user = f"{base_url}/posts?userId={user_id}"
    response = requests.get(url_posts_por_user)
    if response.status_code == 200:  # significa OK!
        data = response.json()
        posts = []
        for post in data:
            posts.append({'title': post['title'],
                          'body': post['body'],
                          'post_id': post['id']})
        # posts = [{'title': post['title'], 'body': post['body']} for post in data]
        return len(data), posts
    raise ErroListaPosts(f"Falha na listagem dos posts para o user_id {user_id}")


def lista_comentarios_por_post(post_id):
    url_comentarios_por_post = f"{base_url}/posts/{post_id}/comments"
    response = requests.get(url_comentarios_por_post)
    if response.status_code == 200:  # significa OK!
        data = response.json()
        comments = []
        for comment in data:
            comments.append(
                {
                    'name': comment['name'],
                    'email': comment['email'],
                    'body': comment['body'],
                }
            )
        return len(data), comments
    raise ErroListaPostComments(f"Falha na listagem dos comentÃ¡rios para o post_id {post_id}")


user_base = {}

url_users = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url_users)
if response.status_code == 200:
    data = response.json()
    for user in data:
        user_id = user["id"]
        user_name = user['name']
        try:
            num_posts, posts = lista_posts_por_user(user_id)
        except ErroListaPosts as e:
            num_posts = None
            posts = []
            print(e)

        num_comments = 0
        comments = []
        if num_posts:
            for post in posts:
                try:
                    n_post_comments, post_comments = lista_comentarios_por_post(post['post_id'])
                except ErroListaPostComments as e:
                    print(e)
                    n_post_comments = 0
                    post_comments = []

                comments += post_comments
                num_comments += n_post_comments

        user_base[(user_name, user_id)] = {
            "num_posts": num_posts,
            "num_comments": num_comments,
            "posts": posts,
            "comments": comments,
        }
        break
    pprint.pprint(user_base)