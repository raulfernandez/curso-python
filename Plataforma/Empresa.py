class ProyectoNoEncontradoError(Exception):
    pass


class ObjectoEmpresaInvalidoError(Exception):
    pass


class Empresa:
    def __init__(self, nombre: str, projectos: []):
        self.__nombre = nombre
        self.__projectos = projectos

    def agregar_proyecto(self, proyecto_id: str):
        """
        Agrega un proyecto al empresa.
        :param proyecto_id: El identificador del proyecto
        :return:
        """
        self.__proyectos.append(proyecto_id)

    def empezar_proyecto(self, proyecto_id):
        """
        Empieza la ejecución de un projecto.
        :param proyecto_id: El identificador del proyecto que se desea iniciar
        :raise ProyectoNoEncontradoError En el caso que se intente empezar un projecto que no existe
        :return:
        """
        if proyecto_id not in self.__projectos:
            raise ProyectoNoEncontradoError(f"No se ha encontrado un projecto con el id {proyecto_id}")

        pass

    def serializar(self):
        """
        Serializa el objecto Empresa
        i.e.: `microsoft;;adi1,contoso2`

        :return: Una string con el objeto empresa serializado. Las propiedades separadas por `;` y los elementos de las
        listas separadas por `,`.
        """
        # Serializar proyectos
        proyectos = ','.join(self.__proyectos)
        return f'{self.__nombre};{proyectos}'

    @staticmethod
    def desserializar(empresa_str: str):
        props = empresa_str.split(';')
        if len(props) == 6:
            return Empresa(props[0], props[1].split(','))
        else:
            raise ObjectoEmpresaInvalidoError
