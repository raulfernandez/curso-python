from Plataforma.Usuario import Usuario
from json import load, dump
import collections

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


# URL = 'https://jsonplaceholder.typicode.com/'


def main():
    users = load_json('usuarios.json')
    posts = load_json('posts.json')

    for user in users:
        user['posts'] = \
            [post for post in posts if post['userId'] == user['id']][0:2]

    dump_json('usuarios_con_post.json', users)


if __name__ == '__main__':
    main()