import re


class Serializador:
    def serializar(self):
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

    @staticmethod
    def deserializar(serialized_str: str):
        pass
