from Plataforma.Utils import Serializador


class LimiteDeProyectosError(Exception):
    pass


class ObjectoUsuarioInvalidoError(Exception):
    pass


class Usuario(Serializador):
    def __init__(self, login: str, password: str, nombre: str, apellidos: str, puntuacion: float = 5,
                 numero_trabajos: int = 0, proyectos: list = []):
        super().__init__()
        self.__login = login
        self.__password = password
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__puntuacion = puntuacion
        self.__numero_trabajos = numero_trabajos
        self.__proyectos = proyectos

    def agregar_proyecto(self, proyecto_id: str):
        """
        Agrega un proyecto al usuario.
        Nota: Un usuario solo puede tener un maximo de dos proyectos.
        :param proyecto_id: El identificador del proyecto
        :raise LimiteDeProyectosError En el caso que se intente agregar mas de dos proyectos.
        :return:
        """
        if len(self.__proyectos) <= 2:
            self.__proyectos.append(proyecto_id)
        else:
            raise LimiteDeProyectosError('No puedes agregarter mas de dos proyectos.')

    def calificar(self, puntuacion: float):
        """
        Califica al usuario.
        - Añade la puntuacion e incrementa el numero de trabajos

        :param puntuacion: La puntuacion a calificar
        """
        self.__puntuacion += puntuacion
        self.__numero_trabajos += 1

    @property
    def puntuacion(self):
        return self.__puntuacion / self.__numero_trabajos if self.__numero_trabajos != 0 else self.__puntuacion

    @property
    def proyectos(self):
        return ', '.join(self.__proyectos)

    @classmethod
    def deserializar(cls, serialized_str: str):
        init_str = super().deserializar(serialized_str=serialized_str)
        return eval(init_str)

    def to_json(self):
        return super()
