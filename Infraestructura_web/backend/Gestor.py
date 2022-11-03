from Recurso import Recurso
from Categoria import Categoria
from Cliente import Cliente
import json


class Gestor:

    def __init__(self):
        self.recursos = []
        self.categorias = []
        self.clientes = []

    def agregar_recurso(self, codigo, nombre, abreviatura, metrica, tipo, valorxhora):
        pass

    def agregar_categoria(self, codigo, nombre, descripcion, cargatrabajo):
        pass

    def agregar_clientes(self, nit, nombre, usuario, clave, correo):
        pass
