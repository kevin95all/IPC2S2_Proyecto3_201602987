from Recurso import Recurso
from Categoria import Categoria
from Cliente import Cliente
import json


class Gestor:

    def __init__(self):
        self.recursos = []
        self.categorias = []
        self.clientes = []
