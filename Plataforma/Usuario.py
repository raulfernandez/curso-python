class LimiteDeProyectosError(Exception):
    pass


class ObjectoUsuarioInvalidoError(Exception):
    pass


class Usuario:
    def __init__(self, login: str, nombre: str, apellidos: str, puntuacion: float = 5, numero_trabajos: int = 0, proyectos: list = []):
        self.__login = login
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

    def serializar(self):
        """
        Serializa el objecto Usuario
        i.e.: `john123;John;Smith;5.7;10;adi1,contoso2`

        :return: Una string con el objeto usuario serializado. Las propiedades separadas por `;` y los elementos de las
        listas separadas por `,`.
        """
        # Serializar proyectos
        proyectos = ','.join(self.__proyectos)
        return f'{self.__login};{self.__nombre};{self.__apellidos};{self.__puntuacion};{self.__numero_trabajos};{proyectos}'

    @staticmethod
    def deserializar(usuario_str: str):
        """
        Deserializa una string y devuelve un objecto Usuario.

        :param usuario_str: String representando un usuario. i.e.: `john123;John;Smith;5.7;10;adi1,contoso2`
        :return:Usuario Devuelve un objecto Usuario
        """
        props = usuario_str.split(';')
        if len(props) == 6:
            return Usuario(props[0], props[1], props[2], float(props[3]), int(props[4]), props[5].split(','))
        else:
            raise ObjectoUsuarioInvalidoError
