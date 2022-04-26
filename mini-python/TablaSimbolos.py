class TablaSimbolos:

    tabla = []

    nivelActual = 0

    class Ident:

        def __init__(self, identifier, params, isMethod, decl):
            self.identifier = identifier
            self.nivel = TablaSimbolos.nivelActual
            self.params = params
            self.isMethod = isMethod
            self.declCtx = decl

        def getNivel(self):
            return self.nivel

    def __init__(self):
        TablaSimbolos.tabla = []
        TablaSimbolos.nivelActual = - 1

    def insertar(self, identifier, params, isMethod, decl):
        # no se puede insertar un elemento repetido en el mismo nivel
        i = TablaSimbolos.Ident(identifier, params, isMethod, decl)
        self.tabla.append(i)

    def buscar(self, nombre):
        tablaCopy = self.tabla.copy()
        for id1 in tablaCopy:
            if str(id1.identifier) == str(nombre):
                return id1
        return None

    def openScope(self):
        self.nivelActual = self.nivelActual + 1

    # Método lambda de tipo funcional
    def closeScope(self):
        x = lambda n: n.nivel == self.nivelActual
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
            print("Nombre: " + i.identifier + " - " + i.nivel)
            ''' if (s.getType() == 0) print("\tTipo: Indefinido");
            else if (s.getType() == 1) print("\tTipo: Integer\n");'''

        print("----- FIN TABLA ------")
