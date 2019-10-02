from setuptools import setup

setup(
      name='zaragoza_abierta',
      version='0.1',
      description='Ejercicio de la semana 3 dia 3',
      author='Raul Fernandez',
      packages=[],
      license='MIT',
      entry_points={
            'console_scripts': [
                  'zabapp = app'
            ]
      },
      classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ),
      install_requires=['requests', 'html2text', 'snakecase']
      )
