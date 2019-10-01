from Plataforma.Usuario import Usuario
from json import load, dump
import collections
import random


# URL = 'https://jsonplaceholder.typicode.com/'
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
    yield random.shuffle(users)


def first_random_user(users: list) -> dict:
    return shuffled_users(users)[0]


def find_all_post(user, posts) -> list:
    return [post for post in posts if post['userId'] == user['id']]


def main():
    users = load_json('usuarios.json')
    posts = load_json('posts.json')

    print(find_all_post(first_random_user(users), posts))


if __name__ == '__main__':
    main()