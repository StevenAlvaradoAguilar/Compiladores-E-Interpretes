from antlr4 import *

class TablaSimbolos:

    def __init__(self):
        self.tabla = []
        self.nivelActual = 0

    class Ident:

        def __init__(self, identifier, level, isMethod, decl):
            self.token = identifier
            self.level = level
            self.params = None
            self.isMethod = isMethod
            self.declCtx = decl

        def setValue(self, value):
            self.value = value

        def getNivel(self):
            return self.nivel

    def getLevel(self):
        return self.nivelActual

    # ----------------METODOS------------------

    def insertar(self, identifier, level, isMethod, decl):
        # no se puede insertar un elemento repetido en el mismo nivel
        i = self.Ident(identifier, level, isMethod, decl)
        self.tabla.insert(0, i)

    def buscar(self, nombre):
        tablaCopy = self.tabla.copy()
        for id1 in tablaCopy:
            if str(id1.token) == str(nombre):
                return id1
        return None

    def openScope(self):
        self.nivelActual = self.nivelActual + 1

    # Método lambda de tipo funcional
    def closeScope(self):
        x = lambda n: n.level == self.nivelActual
        tablaCopy = self.tabla.copy()
        # Iterar la tabla
        for n in tablaCopy:
            if x(n):
                self.tabla.remove(n)
        self.nivelActual = self.nivelActual - 1

    def imprimir(self):
        print("----- INICIO TABLA ------")
        tablaCopy = self.tabla.copy()
        for i in tablaCopy:
            token = i.token
            print("Nombre: " + i.getText() + " - Nivel:" + str(i.nivel))
        print("----- FIN TABLA ------")
