"""
# Utils Module
"""
import html2text


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


def print_html(html: str):
    """
    Returns the ASCII representation of HTML
    :param html:
    :return:
    """
    h = html2text.HTML2Text()
    return h.handle(html)


def pretty_print(msg: str, style: Colors = Colors.DEFAULT, html=False):
    """
    Prints prettier on the terminal, using terminal colors.
    """
    pretty_msg = print_html(msg) if html else msg
    print(f'{style}{pretty_msg}{Colors.ENDC}')


def print_list(lst: list, style: Colors, html=False):
    """
    Prints a list in a prettier way.
    """
    for i in lst:
        pretty_print(i, style, html)
