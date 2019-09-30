import random

from Plataforma.Empresa import Empresa
from Plataforma.Proyecto import Proyecto
from Plataforma.Usuario import Usuario

PATH = '\\\\192.168.3.14\\Users\\CTA\\Desktop\\fila4 pm\\ProyectoConjunto\\'
USUARIOS_FILE = f'{PATH}usuarios.txt'
EMPRESA_FILE = f'{PATH}empresas.txt'
PROYECTOS_FILE = f'{PATH}proyectos.txt'


class Plataforma:
    def __init__(self):
        self.__usuarios = list()

        # Cargar 'base de datos'
        self.__empresas = self.__cargar_empresas()
        self.__proyectos = self.__cargar_proyectos()
        self.__cargar_usuarios()

    @property
    def usuarios(self):
        return self.__usuarios

    def __cargar_usuarios(self):
        try:
            with open(USUARIOS_FILE, 'rt') as archivo:
                usuarios_str = archivo.readlines()
                self.__usuarios = [Usuario.deserializar(usuario_str) for usuario_str in usuarios_str]
        except Exception as ex:
            print('Problemas cargando los usuarios', ex)

    def __guardar_usuarios(self):
        pass

    def __cargar_empresas(self) -> list:
        # TODO: Lectura de archivo.
        pass

    def __cargar_proyectos(self) -> list:
        # TODO: Lectura de archivo.
        pass

    def registrar_usuario(self, usuario: Usuario):
        # añadir a lista
        self.__usuarios.append(usuario)
        # TODO: escribir en archivo

    def registrar_empresa(self, empresa: Empresa):
        # añadir a lista
        self.__empresas.append(empresa)
        # TODO: escribir en archivo

    def registrar_proyecto(self, proyecto: Proyecto):
        # añadir a lista
        self.__proyectos.append(proyecto)
        # TODO: escribir en archivo

    def mostrar_proyectos(self, categoria: str = None) -> list:
        """
        Muestra lista de proyectos. Si la categoria se ha pasado, la lista devuelta sera filtrada.
        :param categoria: La categoria del proyecto
        :return: Lista de proyectos
        """
        pass

    def inscribir_usuario(self, usuario: Usuario, proyecto: Proyecto):
        """
        Inscribe a un usuario a un proyecto especifico.
        :param usuario: Usuario que quiere inscribirse
        :param proyecto: Proyecto al que el usuario quiere inscribirse
        :return:
        """
        pass

    def __asignar_usuario(self, proyecto: Proyecto):
        """
        Asignar un usuario en funcion de la nota mas alta. A notas iguales, elegir aleatoriamente.
        :param proyecto: El proyecto donde asignar al usuario
        """
        pass

    def entregar_proyecto(self, proyecto: Proyecto):
        """
        Entrega o libera un proyecto de un usuario.
        :param proyecto: El proyecto a entregar
        """
        pass

    def __evaluar_proyecto(self, proyecto: Proyecto):
        """
        AI que evalua la puntuacion del proyecto
        :param proyecto: El proyecto a evaluar.
        """
        # Obtener el usuario del proyecto
        # Generar puntuacion
        puntuacion = random.random(0, 10)
        # Asignar puntuacion al usuario

    def __liberar_usuario_de_proyecto(self, proyecto: Proyecto):
        pass

    def es_usuario_registrado(self, usuario: str, password: str, es_admin: bool = False) -> bool:
        pass
