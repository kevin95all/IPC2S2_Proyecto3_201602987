class Recurso:

    def __init__(self, codigo, nombre, abreviatura, metrica, tipo, valorxhora):
        self.codigo = codigo
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.metrica = metrica
        self.tipo = tipo
        self.valorxhora = valorxhora

    def getRecurso(self):
        return self
