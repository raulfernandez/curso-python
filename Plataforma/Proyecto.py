from Plataforma import Usuario
from Plataforma.Utils import Serializador


class LimiteDeUsuariosError(Exception):
    pass


class ObjectoProyectoInvalidoError(Exception):
    pass


MAX_NUMERO_USUARIOS = 3


class Proyecto(Serializador):
    def __init__(self, empresa, titulo: str, id: str, categoria="", candidatos=[], asignado=None, estado=False,
                 max_numero_candidatos=MAX_NUMERO_USUARIOS):
        self.__empresa = empresa
        self.__titulo = titulo
        self.__id = id
        self.__usuario_asignado = asignado
        self.__proyecto_finalizado = estado
        self.__categoria = categoria
        self.__candidatos = candidatos
        self.__max_numero_candidatos = max_numero_candidatos

    @property
    def empresa(self):
        return self.__empresa

    @property
    def categoria(self):
        return self.__categoria

    @property
    def identificador(self):
        return self.__id

    @property
    def titulo(self):
        return self.__titulo

    @property
    def asignado(self):
        return self.__usuario_asignado

    @property
    def finalizado(self):
        return self.__proyecto_finalizado

    @property
    def disponible(self):
        return self.__usuario_asignado is None and len(self.__usuarios) < self.__max_numero_candidatos

    def agregar_candidato(self, candidato: Usuario):
        if not self.__es_equipo_lleno():
            self.__candidatos.append(candidato)
        else:
            raise LimiteDeUsuariosError("No se pueden añadir más candidatos al proyecto")

    def elegir_candidato(self):
        if len(self.__usuarios):
            return False
        else:
            self.__mi_algoritmo_de_asignacion()

    def finalizar_proyecto(self):
        self.__proyecto_finalizado = True

    def __mi_algoritmo_de_asignacion(self):
        elegido = None
        for candidato in self.__candidatos:
            if elegido is None or candidato.puntuacion > elegido.puntuacion:
                elegido = candidato
        self.__usuario_asignado = elegido

    def __es_equipo_lleno(self) -> bool:
        return len(self.__usuarios) > self.__max_numero_candidatos

    @classmethod
    def deserializar(cls, serialized_str: str):
        init_str = super().deserializar(serialized_str=serialized_str)
        return eval(init_str)
