class TablaSimbolos:
    tabla = []
    tablaCopy = tabla.copy()

    nivelActual = int

    class Ident:

        def __int__(self, t, p, im, decl):
            self.tok = t
            self.nivel = TablaSimbolos.nivelActual
            self.valor = 0
            self.params = p
            self.isMethod = im
            self.declCtx = decl

        def setValue(self, v):
            self.valor = v

        def getNivel(self):
            return self.nivel

    def __init__(self):
        TablaSimbolos.tabla = []
        TablaSimbolos.nivelActual = -1

    def insertar(self, id, p, im, decl):
        # no se puede insertar un elemento repetido en el mismo nivel
        i = TablaSimbolos.Ident(id, p, im, decl)
        self.tabla.append(i)

    def buscar(self, nombre):
        for id1 in self.tablaCopy:
            if id1.nombre == nombre:
                return id1.nombre
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
            print("Nombre: " + str(i.text) + " - " + str(i.nivelActual))
            ''' if (s.getType() == 0) print("\tTipo: Indefinido");
            else if (s.getType() == 1) print("\tTipo: Integer\n");'''

        print("----- FIN TABLA ------")
