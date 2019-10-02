"""
# Utils Module
"""


import html2text


def print_html(html: str):
    h = html2text.HTML2Text()
    return h.handle(html)


class Colors:
    DEFAULT = ''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def pretty_print(msg: str, style: Colors = Colors.DEFAULT, html=False):
    pretty_msg = print_html(msg) if html else msg
    print(f'{style}{pretty_msg}{Colors.ENDC}')


def print_list(lst: list, style: Colors, html=False):
    for i in lst:
        pretty_print(i, style, html)
