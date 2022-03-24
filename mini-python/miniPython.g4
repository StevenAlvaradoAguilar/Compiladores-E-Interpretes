grammar miniPython;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from miniPythonParser import miniPythonParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: miniPythonLexer = lexer

    def pull_token(self):
        return super(miniPythonLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NEWLINE, miniPythonParser.INDENT, miniPythonParser.DEDENT, False)
    return self.denter.next_token()
}

//el DEDENT debe llevar antes un NEWLINE
program : INDENT statement | statement program NEWLINE DEDENT ;
statement : defStatement | ifStatement | returnStatement | printStatement | whileStatement |
            forStatement | assignStatement | functionCallStatement | expressionStatement;
defStatement : DEF ID ( argList ) DOSPUNT sequence;
argList : (ID moreArgs)*;
moreArgs : (COMA ID moreArgs)*;
ifStatement : IF expression DOSPUNT sequence
              ELSE DOSPUNT sequence;
whileStatement : WHILE expression DOSPUNT sequence;
forStatement : FOR expression IN expressionList DOSPUNT sequence;
returnStatement : RETURN expression NEWLINE;
printStatement : PRINT expression NEWLINE;
assignStatement : ID EQUAL expression NEWLINE;
functionCallStatement : primitiveExpression ( expressionList ) NEWLINE;
expressionStatement : expressionList NEWLINE;
sequence : INDENT moreStatements DEDENT;
moreStatements : statement (statement)*;
expression : additionExpression comparison;
comparison : ((MENQUE | MAYQUE | MENQUEEQUAL | MAYQUEEQUAL | EQUALEQUAL) additionExpression)*;
additionExpression : multiplicationExpression additionFactor;
additionFactor : ((MAS|MEN) multiplicationExpression)*;
multiplicationExpression : elementExpression multiplicationFactor;
multiplicationFactor : ((MULT | DIV) elementExpression)*;
elementExpression : primitiveExpression elementAccess;
elementAccess : ( CIZQ expression CDER )*;
expressionList : expression moreExpressions;
moreExpressions : (COMA expression)*;
primitiveExpression : ID | FLOAT | CHARCONTS | STRING | ID ((expressionList)*) | (expression)
| listExpression | LEN PIZQ expression PDER;
listExpression : CIZQ expressionList CDER;


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//símbolos
COMA : ',';
PyCOMA : ';';
ASIGN : ':=';
PIZQ : '(';
PDER : ')';
CIZQ : '[';
CDER : ']';
VIR : '~';
DOSPUNT : ':';
MAS : '+';
MULT : '*';
MEN : '-';
DIV : '/';
POT : '**';
MOD : '%';
MENQUE : '<';
MAYQUE : '>';
MENQUEEQUAL : '<=';
MAYQUEEQUAL : '>=';
EQUALEQUAL : '==';
EQUAL : '=';
//FALTAN OTROS

//palabras reservadas
IF : 'if';
THEN : 'then';
ELSE : 'else';
WHILE : 'while';
DO : 'do';
LET : 'let';
IN : 'in';
BEGIN : 'begin';
END : 'end';
CONST : 'const';
VAR : 'var';
DEF : 'def';
LEN : 'len';

//otros tokens
NUM : DIGIT DIGIT*;
ID : LETTER (LETTER | DIGIT)*;
STRING :  LETTER (LETTER | LETTER)*;
FLOAT : DIGIT;

fragment DIGIT : [0-9];
fragment LETTER : [a-z];

NEWLINE: ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' '* with '\t'*

WS  :   [ +\r\n\t] -> skip ;