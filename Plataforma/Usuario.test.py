import unittest

from Plataforma.Usuario import Usuario, LimiteDeProyectosError


class TestUsuario(unittest.TestCase):
    def test_usuario_agrega_proyecto(self):
        test_usuario = Usuario('test', 'test', 'test')

        try:
            test_usuario.agregar_proyecto('test_proyecto1')
            test_usuario.agregar_proyecto('test_proyecto2')
            self.assertEqual(test_usuario.proyectos, 'test_proyecto1, test_proyecto2')
            test_usuario.agregar_proyecto('test_proyecto2')
        except Exception as ex:
            self.assertEqual(type(ex), LimiteDeProyectosError)


if __name__ == '__main__':
    unittest.main()
