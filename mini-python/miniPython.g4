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
program : statement (statement)*                                                                   #programMP;
statement : (defStatement | ifStatement | returnStatement | printStatement | whileStatement
            | forStatement | assignStatement | functionCallStatement | expressionStatement)        #statementMP;
defStatement : DEF IDENTIFIER PIZQ argList PDER DOSPUNT sequence                                   #defStatementMP;
argList : (IDENTIFIER moreArgs | )                                                                 #argListMP;
moreArgs : (COMA IDENTIFIER)*                                                                      #moreArgsMP;
ifStatement : (IF expression DOSPUNT sequence ELSE DOSPUNT sequence |
              IF expression DOSPUNT sequence)                                                      #ifStatementMP;
whileStatement : WHILE expression DOSPUNT sequence                                                 #whileStatementMP;
forStatement : FOR expression IN expressionList DOSPUNT sequence                                   #forStatementMP;
returnStatement : RETURN expression NEWLINE                                                        #returnStatementMP;
printStatement : PRINT PIZQ expression PDER NEWLINE                                                #printStatementMP;
assignStatement : IDENTIFIER (ASIGN | MASEQUAL | MENEQUAL) expression NEWLINE                      #assignStatementMP;
functionCallStatement : primitiveExpression PIZQ expressionList PDER NEWLINE                       #functionCallStatementMP;
expressionStatement : expressionList NEWLINE                                                       #expressionStatementMP;
sequence : INDENT moreStatements DEDENT                                                            #sequenceMP;
moreStatements : (statement)+                                                                      #moreStatementsMP;
expression : additionExpression comparison                                                         #expressionMP;
comparison : ((MENQUE | MAYQUE | MENQUEEQUAL | MAYQUEEQUAL | MULTEQUAL | DIVEQUAL
| EQUALEQUAL) additionExpression)*                                                                 #comparisonMP;
additionExpression : multiplicationExpression additionFactor                                       #additionExpressionMP;
additionFactor : ((MAS|MEN) multiplicationExpression)*                                             #additionFactorMP;
multiplicationExpression : elementExpression multiplicationFactor                                  #multiplicationExpressionMP;
multiplicationFactor : ((MULT | DIV) elementExpression)*                                           #multiplicationFactorMP;
elementExpression : (primitiveExpression elementAccess | primitiveExpression)                      #elementExpressionMP;
elementAccess : ( CIZQ expression CDER )+                                                          #elementAccessMP;
expressionList : (expression moreExpressions | )                                                   #expressionListMP;
moreExpressions : (COMA expression)*                                                               #moreExpressionsMP;
primitiveExpression : (MEN? INTEGER | MEN? FLOAT | CHARCONTS | STRING | IDENTIFIER ( PIZQ
   expressionList PDER | ) | PIZQ expression PDER | listExpression | LEN PIZQ expression PDER)     #primitiveExpressionMP;
listExpression : CIZQ expressionList CDER                                                          #listExpressionMP;


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//símbolos
COMA : ',';
PyCOMA : ';';
ASIGN : '=';
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
MASEQUAL : '+=';
MENEQUAL : '-=';
MULTEQUAL : '*=';
DIVEQUAL : '/=';
HASH  : '\n';

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
DEF : 'def';
LEN : 'len';
FOR : 'for';
RETURN : 'return';
PRINT : 'print';

//otros tokens
INTEGER : DIGITNOTZERO DIGIT* | '0';
IDENTIFIER : LETTER (LETTER | DIGIT)*;

STRING :  '\'' (LETTER | DIGIT | SIMBOLS | SPECIALSIMBOLS)* '\'' | ('"' (LETTER |DIGIT | SIMBOLS | SPECIALSIMBOLS)* '"');
FLOAT : ((DIGITNOTZERO | '0' ) '.' (DIGIT)+ )| (DIGITNOTZERO (DIGIT)+ '.' DIGIT+);
CHARCONTS : '\'' ((LETTER | DIGIT | SIMBOLS | SPECIALSIMBOLS) | ) '\'';

//COMENTARIOS
COMENTLINEA : ('#' ~[\r\n]* NEWLINE)-> skip;
COMENTMULTILINEA : ('"""' .+? '"""' NEWLINE)-> skip;

fragment DIGIT : [0-9];
fragment LETTER : [a-z] | [A-Z] | '_';
fragment DIGITNOTZERO : [1-9];
fragment SIMBOLS : COMA | PyCOMA | ASIGN | PIZQ | PDER | CIZQ | CDER | VIR | DOSPUNT | MAS | MULT | ' '|
MEN | DIV | POT | MOD | MENQUE | MAYQUE | MENQUEEQUAL | MAYQUEEQUAL | EQUALEQUAL | ASIGN | MASEQUAL | MENEQUAL |
MULTEQUAL | DIVEQUAL | HASH;
fragment SPECIALSIMBOLS : '!' | '#' | '$' | '^' | '&' | '_' | '?' | '%' | '`' | '@' | '¿' | 'ñ';

NEWLINE: ('\r'? '\n' (' ' | '\t') *); //For tabs just switch out ' '* with '\t'*

WS  :   [ +\r\n\t] -> skip ;
