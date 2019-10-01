from Plataforma.Usuario import Usuario
from json import load, dumps, dump
import collections
import random
import requests


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def serializar_usuario_a_json():
    usr = Usuario('jhons', 'John', 'Smith', 4.9, 8, ['actme_proj1', 'foo_contoso'])
    # esto da error. Hay que actualizar usuario class.
    str_json = dumps(usr)
    print(str_json)


def serializar_usuario_a_json2():
    usr = Usuario('jhons', 'John', 'Smith', 4.9, 8, ['actme_proj1', 'foo_contoso'])
    # esto da error. Hay que actualizar usuario class.
    str_json = dumps(usr.__dict__)
    print(str_json)


def procesar(a: int):

    def inner_procesar(b: int) -> int:
        return a + b

    return inner_procesar


def load_json(file_name):
    obj = {}

    try:
        json_file = open(f'C:/git/curso-python/json/{file_name}', 'r')
        obj = load(json_file)
        json_file.close()
    except Exception as ex:
        print('Error', ex)

    return obj


def dump_json(file_name, obj):
    try:
        json_file = open(f'C:/git/curso-python/json/{file_name}', 'w')
        dump(obj, json_file)
        json_file.close()
    except Exception as ex:
        print('Error', ex)


def exercise1(users, posts):
    for user in users:
        user['posts'] = \
            [post for post in posts if post['userId'] == user['id']][0:2]

    dump_json('usuarios_con_post.json', users)


def shuffled_users(users: list) -> list:
    users_copy = users.copy()
    random.shuffle(users_copy)
    return users_copy


def first_random_user(users: list) -> dict:
    return shuffled_users(users)[0]


def find_all_post(user, posts) -> list:
    return [post for post in posts if post['userId'] == user['id']]


def print_posts(posts):
    [print_post(post) for post in posts]


def print_post(post):
    print("-" * 79)
    print(f'\t{Colors.OKBLUE}{post["title"]}{Colors.ENDC}\n')
    print(f'{Colors.WARNING}{post["body"]}{Colors.ENDC}')


def ejercicio2():
    users = load_json('usuarios.json')
    posts = load_json('posts.json')

    print_posts(find_all_post(first_random_user(users), posts))


def get_post_comments(post_id):
    data = requests.request('GET', f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
    return data.json()


def get_id_from_longest_post(posts):
    max_len = 0
    post_id = None

    for post in posts:
        if max_len < len(post['body']):
            max_len = len(post['body'])
            post_id = post['id']

    return post_id


def main():
    posts = load_json('posts.json')
    print(get_id_from_longest_post(posts), get_post_comments(get_id_from_longest_post(posts)))
