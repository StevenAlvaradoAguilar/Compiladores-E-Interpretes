from generated.miniPythonParser import *
from antlr4.ParserRuleContext import *

class TablaSimbolos:

    global tabla
    tabla= [ ]

    global nivelActual
    nivelActual = int

    class Ident:
        global tok
        tok= miniPythonParser.Token
        global nivel
        miniPythonParser.nivel = int
        global valor
        miniPythonParser.valor = int
        global params
        miniPythonParser.params = [miniPythonParser.IdDeclarationContext]
        global isMethod
        miniPythonParser.isMethod = bool
        global declCtx
        miniPythonParser.declCtx = ParserRuleContext

        def Ident(self, t, p, im, decl):
            self.tok = t
            self.nivel = nivelActual
            self.valor = 0
            self.params = p
            self.isMethod = im
            self.declCtx = decl

        def setValue(self, v):
            self.valor = v


        def getNivel(self):
            return self.nivel


    class TablaSimbolos:
        tabla = []
        super().nivelActual=-1

    id = Token
    p = [miniPythonParser.IdDeclarationContext]
    im = bool
    decl = ParserRuleContext
    def insertar(self, id, p, im, decl):
        #no se puede insertar un elemento repetido en el mismo nivel
        i = self.Ident
        i = self.Ident(id,p,im,decl)
        tabla.addFirst(i)

    def buscar(self, "nombre"):
        self.Ident = 0
        temp = self.Ident
        Object = id
        for(id : tabla):
            if (((self.Ident)id).tok.getText().equals("nombre")):
                return ((self.Ident)id)
        return temp

    def openScope(self):
        self.nivelActual = nivelActual + 1

    #Método lambda de tipo funcional
    def closeScope(self):
        tabla.remove(n -> (self.Ident.nivel == nivelActual))
        self.nivelActual = nivelActual - 1

    class imprimir:
        print("----- INICIO TABLA ------");
        for _ in tabla:
            s = Token
            s = Token ((Ident) tabla.__getitem__(i).tok
            print("Nombre: " + s.text + " - " + ((Ident) tabla.get(i)).nivel + " - " + ((Ident) tabla.get(i)).type)
            ''' if (s.getType() == 0) print("\tTipo: Indefinido");
            else if (s.getType() == 1) print("\tTipo: Integer\n");'''

        print("----- FIN TABLA ------")