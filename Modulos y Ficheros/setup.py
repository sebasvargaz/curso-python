from setuptools import setup
from struct import pack

setup(
    
    name='Mensajes',
    version='1.0',
    description='Un paquete para saludar y despedir',
    author='Héctor Costa Guzman',
    author_email='hola@sebasrivar',
    url='http:www.facebook.com/sebas.varg5',
    packages=['mensajes', 'mensajes.hola', 'mensajes.adios'],
    scripts=['test.py']
)

