// 2211927
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

// ! ---------------- LEXER ----------------------- */

// Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
LESS_EQUAL: '<=';
GREATER: '>';
GREATER_EQUAL: '>=';

// Logical Operators
OR  : '||';
AND : '&&';
NOT : '!';
SHORT_DECL: ':=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
ASSIGN: '=';
DOT: '.';

// Delimiters
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
LBRACE: '{';
RBRACE: '}';
COMA: ',';
SEMI: ';' | '\r'? '\n' {
    if self.preType in {
        self.RPAREN, self.RBRACE, self.RBRACKET, 
        self.INT_LIT, 
        self.FLOAT_LIT, self.STRING_LIT, self.TRUE, 
        self.FALSE, self.ID, self.BREAK, 
        self.CONTINUE, self.RETURN, self.NIL
    }:
        self.text = ';'
    else:
        self.skip()
};
COLON: ':';

// ID and Literals
ID: [a-zA-Z_][a-zA-Z0-9_]*;

INT_LIT: DEC_LIT | BIN_LIT | OCT_LIT | HEX_LIT;
fragment DEC_LIT: ('0' | [1-9] [0-9]*);
fragment BIN_LIT: '0' [Bb] [01]+;
fragment OCT_LIT: '0' [Oo] [0-7]+;
fragment HEX_LIT: '0' [Xx] [0-9A-Fa-f]+;

FLOAT_LIT: DEC_PART '.' DEC_PART? EXP_PART?;
fragment DEC_PART: [0-9]+;
fragment EXP_PART: [Ee] [+-]? DEC_PART;

STRING_LIT: '"' STR_CHAR* '"';
fragment ESCAPED_VALUE: '\\' [ntr"\\];
fragment STR_CHAR: ~[\r\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [rnt"\\];
fragment ESC_ILLEGAL: [\r] | '\\' ~[rnt'\\];

// Whitespace
WS: [ \t\r\f]+ -> skip;

// Comments
COMMENT : '/*' (COMMENT|.)*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Errors
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[:-1])
    else:
        raise UncloseString(self.text)
};
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text)
};


//! ---------------- PARSER ----------------------- */
program: list_declared_statement EOF;
list_declared_statement: declared_statement SEMI list_declared_statement | declared_statement SEMI;

declared_statement: var_decl | const_decl | func_decl | struct_decl | interface_decl | method_decl;
const_decl: CONST ID ASSIGN expression;
var_decl: VAR ID (type_return | ASSIGN expression | type_return ASSIGN expression);
primitive_type: INT | FLOAT | STRING | BOOLEAN;
numeric_literal: INT_LIT | FLOAT_LIT;
boolean_literal: TRUE | FALSE;

// Array
primitive_literal: NIL | struct_literal | numeric_literal | boolean_literal | STRING_LIT; // primitive_literal: NIL | struct_literal | numeric_literal | boolean_literal | STRING_LIT;
literal: primitive_literal | array_literal;
array_bracket: LBRACKET (INT_LIT | ID) RBRACKET array_bracket | LBRACKET (INT_LIT | ID) RBRACKET;
type_return: array_bracket? (ID | primitive_type);
array_literal: array_bracket (ID | primitive_type) LBRACE array_lit_elements RBRACE;
array_lit_elements: array_lit_element COMA array_lit_element | array_lit_element;
array_lit_element:  LBRACE array_lit_element RBRACE | array_lit_element COMA array_lit_element | (primitive_literal | ID);

// Function and Method declaration
func_decl: FUNC ID LPAREN method_params? RPAREN type_return? LBRACE statements_in_block? RBRACE;
method_decl: FUNC LPAREN ID ID RPAREN ID LPAREN method_params? RPAREN expression? (type_return)? LBRACE statements_in_block RBRACE;

// // Struct and Interface declaration
struct_literal: ID LBRACE struct_element? RBRACE;
struct_element: ID COLON expression COMA struct_element | ID COLON expression;
interface_decl: TYPE ID INTERFACE LBRACE method_interface_decl RBRACE;
method_interface_decl: ID LPAREN method_params? RPAREN type_return? (SEMI) method_interface_decl | ID LPAREN method_params? RPAREN type_return? (SEMI);
method_params: ID type_return? COMA method_params | ID type_return;
struct_decl: TYPE ID STRUCT LBRACE struct_decl_elements RBRACE;
struct_decl_elements: struct_decl_element (SEMI) struct_decl_elements | struct_decl_element (SEMI);
struct_decl_element: ID type_return;

// Expression
list_expression: expression COMA list_expression | expression;
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (EQUAL | NOT_EQUAL | LESS | GREATER | LESS_EQUAL | GREATER_EQUAL) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: (NOT | SUB) expression5 | expression6;
expression6: expression6 DOT ID | expression6 DOT ID LPAREN list_expression? RPAREN | expression6 LBRACKET expression RBRACKET | expression7;
expression7: ID | literal | func_call | LPAREN expression RPAREN;
func_call: ID LPAREN list_expression? RPAREN;

// Statement
list_statement: statement SEMI list_statement | statement SEMI;
statement: declared_statement | assign_statement | if_statement | for_statement | call_statement | return_statement;
full_statement: statement | break_statement | continue_statement;
statements_in_block: full_statement SEMI statements_in_block | full_statement SEMI;

// Assignment Statement
lhs: lhs DOT ID | lhs LBRACKET expression RBRACKET | ID;
op_assign: SHORT_DECL | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
assign_statement: lhs op_assign expression;

// If Statement
else_if_el: ELSE IF LPAREN expression RPAREN LBRACE statements_in_block? RBRACE;
else_if_statement:  else_if_el | else_if_el else_if_statement;
if_statement: IF LPAREN expression RPAREN LBRACE statements_in_block? RBRACE else_if_statement? (ELSE LBRACE statements_in_block? RBRACE)?;

// For Statement
for_statement: FOR (basic_for_statement | init_for_statement | range_for_statement);
basic_for_statement: expression LBRACE statements_in_block? RBRACE;
update_part: ID (SHORT_DECL | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN) expression;
init_for_statement: ((ID (SHORT_DECL | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN) expression) | VAR ID type_return? ASSIGN expression) (SEMI) expression (SEMI) update_part LBRACE statements_in_block? RBRACE;
range_for_statement: ID COMA ID SHORT_DECL RANGE (lhs | INT_LIT | struct_literal | array_literal) LBRACE statements_in_block? RBRACE;

// Break, Continue, Call and Return Statement
break_statement: BREAK;
continue_statement: CONTINUE;
call_statement: call_statement DOT call_statement | call_statement LBRACKET INT_LIT RBRACKET | call_statement_1;
call_statement_1: ID | func_call;
return_statement: RETURN expression?;


