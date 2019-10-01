import re
import json
from importlib import import_module


def try_parse(val: str) -> str:
    result = ''
    try:
        int(val)
    except ValueError:
        result += f'"{val}"'
    else:
        result += f'{val}'

    return result


class Serializador:
    """
    class: Serializador

    Serializa y deserializa a string.
    """
    def serializar(self):
        """
        Serializa el objecto
        i.e.: `prop1:value1;prop2:val2,val3;prop3:val4`

        :return: Una string con el objeto serializado. Las propiedades separadas por `;`, el nombre de la propiedad y
        el valor de la dicha van separados por `:` y los elementos de los valores de las listas separadas por `,`.
        """
        props = [prop for prop in dir(self) if len(re.split(rf'_{self.__class__.__name__}__(\w+)', prop)) == 3]
        result = ''
        for prop in props:
            prop_name = re.split(rf'_{self.__class__.__name__}__(\w+)', prop)[1]
            prop_type = type(eval(f'self.{prop}'))
            prop_value = eval(f'self.{prop}')

            if prop_type == list:
                result += f'{prop_name}:'
                result += ','.join(prop_value)
                result += ';'
            else:
                result += f'{prop_name}:{prop_value};'

        return result

    @classmethod
    def deserializar(cls, serialized_str: str):
        """
        Deserializa una string y devuelve un objecto.

        :param serialized_str: String representando al objecto.
            i.e.: `prop1:value1;prop2:val2,val3;prop3:val4`
        :return:Usuario Devuelve un objecto
        """
        props = serialized_str.strip('\n').split(';')
        class_name = cls.__name__
        class_init_params = ''
        for prop in props:
            if prop:
                name, value = prop.split(':')
                if value:
                    list_values = value.split(',')
                    if len(list_values) > 1:
                        list_values = list(map(lambda x: try_parse(x), list_values))
                        list_values = ','.join(list_values)
                        class_init_params += f'{name}=[{list_values}]'
                    else:
                        class_init_params += f'{name}={try_parse(value)},'

        class_init = f'{class_name}({class_init_params[0:-1]})'
        return class_init


class JSONSerializador:
    @staticmethod
    def from_json(obj, data):
        obj.__dict__ = json.loads(data)
        return obj

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
