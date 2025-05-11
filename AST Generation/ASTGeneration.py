from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce
from typing import Tuple, List

##! continue update
class ASTGeneration(MiniGoVisitor):
    # program: list_declared_statement EOF;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visitList_declared_statement(ctx.list_declared_statement()))
    
    # list_declared_statement: declared_statement SEMI list_declared_statement | declared_statement SEMI;
    def visitList_declared_statement(self, ctx:MiniGoParser.List_declared_statementContext):
        if ctx.list_declared_statement():
            return [self.visitDeclared_statement(ctx.declared_statement())] + self.visitList_declared_statement(ctx.list_declared_statement())
        else:
            return [self.visitDeclared_statement(ctx.declared_statement())]
    
    # declared_statement: var_decl | const_decl | func_decl | struct_decl | interface_decl | method_decl;
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    # const_decl: CONST ID ASSIGN expression;
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return ConstDecl(ctx.ID().getText(), None, self.visitExpression(ctx.expression()))


    # var_decl: VAR ID (type_return | ASSIGN expression | type_return ASSIGN expression);
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        if ctx.getChildCount() == 3:
            return VarDecl(ctx.ID().getText(), self.visitType_return(ctx.type_return()), None)
        elif ctx.getChildCount() == 4:
            return VarDecl(ctx.ID().getText(), None, self.visitExpression(ctx.expression()))
        else:
            return VarDecl(ctx.ID().getText(), self.visitType_return(ctx.type_return()), self.visitExpression(ctx.expression()))


    # primitive_type: INT | FLOAT | STRING | BOOLEAN;
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        else:
            return None


    # numeric_literal: INT_LIT | FLOAT_LIT;
    def visitNumeric_literal(self, ctx:MiniGoParser.Numeric_literalContext):
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        else:
            return None


    # boolean_literal: TRUE | FALSE;
    def visitBoolean_literal(self, ctx:MiniGoParser.Boolean_literalContext):
        if ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)


    # primitive_literal: NIL | struct_literal | numeric_literal | boolean_literal | STRING_LIT;
    def visitPrimitive_literal(self, ctx:MiniGoParser.Primitive_literalContext):
        if ctx.NIL():
            return NilLiteral()
        elif ctx.struct_literal():
            return self.visitStruct_literal(ctx.struct_literal())
        elif ctx.numeric_literal():
            return self.visitNumeric_literal(ctx.numeric_literal())
        elif ctx.boolean_literal():
            return self.visitBoolean_literal(ctx.boolean_literal())
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        else:
            return None


    # literal: primitive_literal | array_literal;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # array_bracket: LBRACKET (INT_LIT | ID) RBRACKET array_bracket | LBRACKET (INT_LIT | ID) RBRACKET;
    def visitArray_bracket(self, ctx:MiniGoParser.Array_bracketContext):
        if ctx.array_bracket():
            if ctx.ID():
                return [Id(ctx.ID().getText())] + self.visitArray_bracket(ctx.array_bracket())
            else:
                return [IntLiteral(int(ctx.INT_LIT().getText()))] + self.visitArray_bracket(ctx.array_bracket())
        else:
            if ctx.ID():
                return [Id(ctx.ID().getText())]
            else:
                return [IntLiteral(int(ctx.INT_LIT().getText()))]


    # type_return: array_bracket? (ID | primitive_type);
    def visitType_return(self, ctx:MiniGoParser.Type_returnContext):
        if ctx.array_bracket():
            if ctx.ID():
                return ArrayType(self.visitArray_bracket(ctx.array_bracket()), Id(ctx.ID().getText()))
            else:
                return ArrayType(self.visitArray_bracket(ctx.array_bracket()), self.visitPrimitive_type(ctx.primitive_type()))
        else:
            if ctx.ID():
                return Id(ctx.ID().getText())
            else:
                return self.visitPrimitive_type(ctx.primitive_type())



    # array_literal: array_bracket (ID | primitive_type) LBRACE array_lit_elements RBRACE;
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        if ctx.ID():
            return ArrayLiteral(self.visitArray_bracket(ctx.array_bracket()), Id(ctx.ID().getText()), self.visitArray_lit_elements(ctx.array_lit_elements()))
        else:
            return ArrayLiteral(self.visitArray_bracket(ctx.array_bracket()), self.visitPrimitive_type(ctx.primitive_type()), self.visitArray_lit_elements(ctx.array_lit_elements()))


    # array_lit_elements: array_lit_element COMA array_lit_element | array_lit_element;
    def visitArray_lit_elements(self, ctx:MiniGoParser.Array_lit_elementsContext):
        if ctx.getChildCount() == 1:
            return self.visitArray_lit_element(ctx.array_lit_element())
        else:
            return self.visitArray_lit_element(ctx.array_lit_element(0)) + self.visitArray_lit_element(ctx.array_lit_element(1))


    # array_lit_element:  LBRACE array_lit_element RBRACE | array_lit_element COMA array_lit_element | (primitive_literal | ID);
    def visitArray_lit_element(self, ctx:MiniGoParser.Array_lit_elementContext):
        if isinstance(ctx, list):
            if ctx[0].ID():
                return [Id(ctx[0].ID().getText())]
            elif ctx[0].primitive_literal():
                return [self.visitPrimitive_literal(ctx[0].primitive_literal())]
        if ctx.ID():
            return [Id(ctx.ID().getText())]
        elif ctx.primitive_literal():
            return [self.visitPrimitive_literal(ctx.primitive_literal())]
        elif ctx.LBRACE():
            return [self.visitArray_lit_element(ctx.array_lit_element(0))]
        else:
            return self.visitArray_lit_element(ctx.array_lit_element(0)) + self.visitArray_lit_element(ctx.array_lit_element(1))
    
    # param_type: param_type LBRACKET (INT_LIT | ID) RBRACKET| LBRACKET (INT_LIT | ID) RBRACKET param_type| param_type_1;
    def visitParam_type(self, ctx:MiniGoParser.Param_typeContext):
        if ctx.param_type_1():
            return self.visitParam_type_1(ctx.param_type_1())
        else:
            return ArrayType()


    # param_type_1: primitive_type | ID;
    def visitParam_type_1(self, ctx:MiniGoParser.Param_type_1Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visitPrimitive_type(ctx.primitive_type())

    # func_decl: FUNC ID LPAREN method_params? RPAREN type_return? LBRACE statements_in_block? RBRACE;
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        if ctx.method_params():
            if ctx.type_return():
                if ctx.statements_in_block():
                    return FuncDecl(ctx.ID().getText(), self.visitMethod_params(ctx.method_params()), self.visitType_return(ctx.type_return()), self.visitStatements_in_block(ctx.statements_in_block()))
                else:
                    return FuncDecl(ctx.ID().getText(), self.visitMethod_params(ctx.method_params()), self.visitType_return(ctx.type_return()), [])
            else:
                if ctx.statements_in_block():
                    return FuncDecl(ctx.ID().getText(), self.visitMethod_params(ctx.method_params()), VoidType(), self.visitStatements_in_block(ctx.statements_in_block()))
                else:
                    return FuncDecl(ctx.ID().getText(), self.visitMethod_params(ctx.method_params()), VoidType(), [])
        else:
            if ctx.type_return():
                if ctx.statements_in_block():
                    return FuncDecl(ctx.ID().getText(), [], self.visitType_return(ctx.type_return()), self.visitStatements_in_block(ctx.statements_in_block()))
                else:
                    return FuncDecl(ctx.ID().getText(), [], self.visitType_return(ctx.type_return()), [])
            else:
                if ctx.statements_in_block():
                    return FuncDecl(ctx.ID().getText(), [], VoidType(), self.visitStatements_in_block(ctx.statements_in_block()))
                else:
                    return FuncDecl(ctx.ID().getText(), [], VoidType(), [])


    # method_decl: FUNC LPAREN ID ID RPAREN ID LPAREN method_params? RPAREN expression? (type_return)? LBRACE statements_in_block RBRACE;
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        id1 = ctx.ID(0).getText()
        id2 = Id(ctx.ID(1).getText())
        if ctx.method_params():
            if ctx.type_return():
                if ctx.statements_in_block():
                    func = FuncDecl(ctx.ID(2).getText(), self.visitMethod_params(ctx.method_params()), self.visitType_return(ctx.type_return()), self.visitStatements_in_block(ctx.statements_in_block()))
                else:
                    func = FuncDecl(ctx.ID(2).getText(), self.visitMethod_params(ctx.method_params()), self.visitType_return(ctx.type_return()), [])
            else:
                if ctx.statements_in_block():
                    func = FuncDecl(ctx.ID(2).getText(), self.visitMethod_params(ctx.method_params()), VoidType(), self.visitStatements_in_block(ctx.statements_in_block()))
                else:
                    func = FuncDecl(ctx.ID(2).getText(), self.visitMethod_params(ctx.method_params()), VoidType(), [])
        else:
            if ctx.type_return():
                if ctx.statements_in_block():
                    func = FuncDecl(ctx.ID(2).getText(), [], self.visitType_return(ctx.type_return()), self.visitStatements_in_block(ctx.statements_in_block()))
                else:
                    func = FuncDecl(ctx.ID(2).getText(), [], self.visitType_return(ctx.type_return()), [])
            else:
                if ctx.statements_in_block():
                    func = FuncDecl(ctx.ID(2).getText(), [], VoidType(), self.visitStatements_in_block(ctx.statements_in_block()))
                else:
                    func = FuncDecl(ctx.ID(2).getText(), [], VoidType(), [])
        return MethodDecl(id1, id2, func)
    
    # struct_literal: ID LBRACE struct_element? RBRACE;
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        if ctx.struct_element():
            return StructLiteral(ctx.ID().getText(), self.visitStruct_element(ctx.struct_element()))
        else:
            return StructLiteral(ctx.ID().getText(), [])


    # struct_element: ID COLON expression COMA struct_element | ID COLON expression;
    def visitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        if ctx.getChildCount() == 3:
            return [(ctx.ID().getText(), self.visitExpression(ctx.expression()))]
        else:
            return [(ctx.ID().getText(), self.visitExpression(ctx.expression()))] + self.visitStruct_element(ctx.struct_element())

    # interface_decl: TYPE ID INTERFACE LBRACE method_interface_decl RBRACE;
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return InterfaceType(ctx.ID().getText(), self.visitMethod_interface_decl(ctx.method_interface_decl()))


    # method_interface_decl: ID LPAREN method_params? RPAREN type_return? (SEMI) method_interface_decl | ID LPAREN method_params? RPAREN type_return? (SEMI);
    def visitMethod_interface_decl(self, ctx:MiniGoParser.Method_interface_declContext):
        if ctx.method_interface_decl():
            if ctx.type_return():
                if ctx.method_params():
                    list_of_para = self.visitMethod_params(ctx.method_params())
                    if not isinstance(list_of_para, list):
                        list_of_type = [list_of_para]
                    else:
                        list_of_type = []
                        for para in list_of_para:
                            if isinstance(para, ParamDecl):
                                list_of_type.append(para.parType)
                            else:
                                list_of_type.append(para)
                    return [Prototype(ctx.ID().getText(), list_of_type, self.visitType_return(ctx.type_return()))] + self.visitMethod_interface_decl(ctx.method_interface_decl())
                else:
                    return [Prototype(ctx.ID().getText(), [], self.visitType_return(ctx.type_return()))] + self.visitMethod_interface_decl(ctx.method_interface_decl())
            else:
                if ctx.method_params():
                    list_of_para = self.visitMethod_params(ctx.method_params())
                    if not isinstance(list_of_para, list):
                        list_of_type = [list_of_para]
                    else:
                        list_of_type = []
                        for para in list_of_para:
                            if isinstance(para, ParamDecl):
                                list_of_type.append(para.parType)
                            else:
                                list_of_type.append(para)
                    return [Prototype(ctx.ID().getText(), list_of_type, VoidType())] + self.visitMethod_interface_decl(ctx.method_interface_decl())
                else:
                    return [Prototype(ctx.ID().getText(), [], VoidType())] + self.visitMethod_interface_decl(ctx.method_interface_decl())
        else:
            if ctx.type_return():
                if ctx.method_params():
                    list_of_para = self.visitMethod_params(ctx.method_params())
                    if not isinstance(list_of_para, list):
                        list_of_type = [list_of_para]
                    else:
                        list_of_type = []
                        for para in list_of_para:
                            if isinstance(para, ParamDecl):
                                list_of_type.append(para.parType)
                            else:
                                list_of_type.append(para)
                    return [Prototype(ctx.ID().getText(), list_of_type, self.visitType_return(ctx.type_return()))]
                else:
                    return [Prototype(ctx.ID().getText(), [], self.visitType_return(ctx.type_return()))]
            else:
                if ctx.method_params():
                    list_of_para = self.visitMethod_params(ctx.method_params())
                    if not isinstance(list_of_para, list):
                        list_of_type = [list_of_para]
                    else:
                        list_of_type = []
                        for para in list_of_para:
                            if isinstance(para, ParamDecl):
                                list_of_type.append(para.parType)
                            else:
                                list_of_type.append(para)
                    return [Prototype(ctx.ID().getText(), list_of_type, VoidType())]
                else:
                    return [Prototype(ctx.ID().getText(), [], VoidType())]

    # method_params: ID type_return? COMA method_params | ID type_return;
    def visitMethod_params(self, ctx:MiniGoParser.Method_paramsContext):
        if ctx.method_params():
            if ctx.type_return():  
                return [ParamDecl(ctx.ID().getText(), self.visitType_return(ctx.type_return()))] + self.visitMethod_params(ctx.method_params())
            else:
                params = self.visitMethod_params(ctx.method_params())
                if params:
                    param_type = params[0].parType
                    return [ParamDecl(ctx.ID().getText(), param_type)] + params
        else:
            return [ParamDecl(ctx.ID().getText(), self.visitType_return(ctx.type_return()))]

    # struct_decl: TYPE ID STRUCT LBRACE struct_decl_elements RBRACE;
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return StructType(ctx.ID().getText(), self.visitStruct_decl_elements(ctx.struct_decl_elements()), [])


    # struct_decl_elements: struct_decl_element (SEMI) struct_decl_elements | struct_decl_element (SEMI);
    def visitStruct_decl_elements(self, ctx:MiniGoParser.Struct_decl_elementsContext):
        if ctx.struct_decl_elements():
            return [self.visitStruct_decl_element(ctx.struct_decl_element())] + self.visitStruct_decl_elements(ctx.struct_decl_elements())
        else:
            return [self.visitStruct_decl_element(ctx.struct_decl_element())]

    # struct_decl_element: ID type_return;
    def visitStruct_decl_element(self, ctx:MiniGoParser.Struct_decl_elementContext):
        return (ctx.ID().getText(), self.visitType_return(ctx.type_return()))
    
    # list_expression: expression COMA list_expression | expression;
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visitExpression(ctx.expression())
        else:
            left = self.visitExpression(ctx.expression())
            right = self.visitList_expression(ctx.list_expression())
            if isinstance(right, list):
                if isinstance(left, list):
                    return left + right
                else:
                    return [left] + right
            else:
                if isinstance(left, list):
                    return left + [right]
                else:
                    return [left, right]


    # expression: expression OR expression1 | expression1;
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visitExpression1(ctx.expression1())
        op = ctx.OR().getText()
        left = self.visitExpression(ctx.expression())
        right = self.visitExpression1(ctx.expression1())
        return BinaryOp(op, left, right)


    # expression1: expression1 AND expression2 | expression2;
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visitExpression2(ctx.expression2())
        else:
            op = ctx.AND().getText()
            return BinaryOp(op, self.visitExpression1(ctx.expression1()), self.visitExpression2(ctx.expression2()))


    # expression2: expression2 (EQUAL | NOT_EQUAL | LESS | GREATER | LESS_EQUAL | GREATER_EQUAL) expression3 | expression3;
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visitExpression3(ctx.expression3())
        else:
            op = ctx.getChild(1).getText()
            return BinaryOp(op, self.visitExpression2(ctx.expression2()), self.visitExpression3(ctx.expression3()))


    # expression3: expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visitExpression4(ctx.expression4())
        else:
            op = ctx.getChild(1).getText()
            return BinaryOp(op, self.visitExpression3(ctx.expression3()), self.visitExpression4(ctx.expression4()))


    # expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visitExpression5(ctx.expression5())
        else:
            op = ctx.getChild(1).getText()
            return BinaryOp(op, self.visitExpression4(ctx.expression4()), self.visitExpression5(ctx.expression5()))


    # expression5: (NOT | SUB) expression5 | expression6;
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visitExpression6(ctx.expression6())
        else:
            op = ctx.getChild(0).getText()
            return UnaryOp(op, self.visitExpression5(ctx.expression5()))


    # expression6: expression6 DOT ID | expression6 DOT ID LPAREN list_expression? RPAREN | expression6 LBRACKET expression RBRACKET | expression7;
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visitExpression7(ctx.expression7())
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visitExpression6(ctx.expression6()), ctx.ID().getText())
        elif ctx.getChildCount() > 4:
            if ctx.list_expression():
                return MethCall(self.visitExpression6(ctx.expression6()), ctx.ID().getText(), self.visitList_expression(ctx.list_expression()))
            else:
                return MethCall(self.visitExpression6(ctx.expression6()), ctx.ID().getText(), [])
        else:
            expression6 = self.visit(ctx.expression6())
            if type(expression6) == ArrayCell:
                return ArrayCell(expression6.arr, expression6.idx  + [self.visit(ctx.expression())])
            return ArrayCell(expression6, [self.visit(ctx.expression())])


    # expression7: ID | literal | func_call | LPAREN expression RPAREN;
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.func_call():
            return self.visitFunc_call(ctx.func_call())
        else:
            return self.visitExpression(ctx.expression())


    # func_call: ID LPAREN list_expression? RPAREN;
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        if ctx.list_expression():
            list_expression = self.visitList_expression(ctx.list_expression())
            if isinstance(list_expression, list):
                return FuncCall(ctx.ID().getText(), list_expression)
            else:
                return FuncCall(ctx.ID().getText(), [list_expression])
        else:
            return FuncCall(ctx.ID().getText(), [])
        
    # list_statement: statement SEMI list_statement | statement SEMI;
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if ctx.list_statement():
            return [self.visitStatement(ctx.statement())] + self.visitList_statement(ctx.list_statement())
        else:
            return [self.visitStatement(ctx.statement())]


    # statement: declared_statement | assign_statement | if_statement | for_statement | call_statement | return_statement;
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # full_statement: statement | break_statement | continue_statement;
    def visitFull_statement(self, ctx:MiniGoParser.Full_statementContext):
        return self.visitChildren(ctx)


    # statements_in_block: full_statement SEMI statements_in_block | full_statement SEMI;
    def visitStatements_in_block(self, ctx:MiniGoParser.Statements_in_blockContext):
        statements = []
        while ctx is not None:
            statements.append(self.visitFull_statement(ctx.full_statement()))
            ctx = ctx.statements_in_block()
        return Block(statements)


    # lhs: lhs DOT ID | lhs LBRACKET expression RBRACKET | ID;
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visitLhs(ctx.lhs()), ctx.ID().getText())
        else:
            lhs = self.visitLhs(ctx.lhs())
            if type(lhs) == ArrayCell:
                return ArrayCell(lhs.arr, lhs.idx  + [self.visit(ctx.expression())])
            return ArrayCell(lhs, [self.visit(ctx.expression())])


    # op_assign: SHORT_DECL | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
    def visitOp_assign(self, ctx:MiniGoParser.Op_assignContext):
        return ctx.getText()


    # assign_statement: lhs op_assign expression;
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        op = self.visitOp_assign(ctx.op_assign())
        lhs = self.visitLhs(ctx.lhs())
        rhs = self.visitExpression(ctx.expression())
        if op == ':=':
            return Assign(lhs, rhs)
        else:
            return Assign(lhs, BinaryOp(op[:-1], lhs, rhs))

    def recursive_if(self, list_else_if_statement:List[Tuple[Expr,Block]], else_statement: Block):
        if len(list_else_if_statement) == 0:
            return else_statement
        exp, block = list_else_if_statement[0]
        return If(exp, block, self.recursive_if(list_else_if_statement[1:], else_statement))

    # else_if_el: ELSE IF LPAREN expression RPAREN LBRACE statements_in_block? RBRACE;
    def visitElse_if_el(self, ctx: MiniGoParser.Else_if_elContext):
        condition = self.visitExpression(ctx.expression())
        block = self.visitStatements_in_block(ctx.statements_in_block())
        return (condition, block)


    # else_if_statement:  else_if_el | else_if_el else_if_statement;
    def visitElse_if_statement(self, ctx: MiniGoParser.Else_if_statementContext):
        first_else_if = self.visitElse_if_el(ctx.else_if_el())
        rest_else_if = self.visitElse_if_statement(ctx.else_if_statement()) if ctx.else_if_statement() else []
        return [first_else_if] + rest_else_if


    # if_statement: IF LPAREN expression RPAREN LBRACE statements_in_block? RBRACE else_if_statement? (ELSE LBRACE statements_in_block? RBRACE)?;
    def visitIf_statement(self, ctx: MiniGoParser.If_statementContext):
        condition = self.visitExpression(ctx.expression())
        then_block = self.visitStatements_in_block(ctx.statements_in_block(0))

        # Lấy danh sách else-if
        list_else_if = []
        if ctx.else_if_statement():
            list_else_if = self.visitElse_if_statement(ctx.else_if_statement())

        # Lấy else block nếu có
        else_block = None
        if ctx.ELSE():
            else_block = self.visitStatements_in_block(ctx.statements_in_block(1))

        return If(condition, then_block, self.recursive_if(list_else_if, else_block))


    # for_statement: FOR (basic_for_statement | init_for_statement | range_for_statement);
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # basic_for_statement: expression LBRACE statements_in_block? RBRACE;
    def visitBasic_for_statement(self, ctx:MiniGoParser.Basic_for_statementContext):
        return ForBasic(self.visitExpression(ctx.expression()), self.visitStatements_in_block(ctx.statements_in_block()))


    # update_part: ID (SHORT_DECL | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN) expression;
    def visitUpdate_part(self, ctx:MiniGoParser.Update_partContext):
        if ctx.SHORT_DECL():
            return Assign(Id(ctx.ID().getText()), self.visitExpression(ctx.expression()))
        else:
            return Assign(Id(ctx.ID().getText()), BinaryOp(ctx.getChild(1).getText()[:-1], Id(ctx.ID().getText()), self.visitExpression(ctx.expression())))


    # init_for_statement: ((ID (SHORT_DECL | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN) expression) | VAR ID type_return? ASSIGN expression) (SEMI) expression (SEMI) update_part LBRACE statements_in_block? RBRACE;
    def visitInit_for_statement(self, ctx:MiniGoParser.Init_for_statementContext):
        if ctx.VAR():
            if ctx.type_return():
                return ForStep(VarDecl(ctx.ID().getText(), self.visitType_return(ctx.type_return()), self.visitExpression(ctx.expression(0))), self.visitExpression(ctx.expression(1)), self.visitUpdate_part(ctx.update_part()), self.visitStatements_in_block(ctx.statements_in_block()))
            else:
                return ForStep(VarDecl(ctx.ID().getText(), None, self.visitExpression(ctx.expression(0))), self.visitExpression(ctx.expression(1)), self.visitUpdate_part(ctx.update_part()), self.visitStatements_in_block(ctx.statements_in_block()))
        else:
            if ctx.SHORT_DECL():
                return ForStep(Assign(Id(ctx.ID().getText()), self.visitExpression(ctx.expression(0))), self.visitExpression(ctx.expression(1)), self.visitUpdate_part(ctx.update_part()), self.visitStatements_in_block(ctx.statements_in_block()))
            else:
                return ForStep(Assign(Id(ctx.ID().getText()), BinaryOp(ctx.getChild(1).getText()[:-1], Id(ctx.ID().getText()), self.visitExpression(ctx.expression(0)))), self.visitExpression(ctx.expression(1)), self.visitUpdate_part(ctx.update_part()), self.visitStatements_in_block(ctx.statements_in_block()))



    # range_for_statement: ID COMA ID SHORT_DECL RANGE (lhs | INT_LIT | struct_literal | array_literal) LBRACE statements_in_block? RBRACE;
    def visitRange_for_statement(self, ctx:MiniGoParser.Range_for_statementContext):
        if ctx.struct_literal():
            return ForEach(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), self.visit(ctx.struct_literal()), self.visitStatements_in_block(ctx.statements_in_block()))
        elif ctx.INT_LIT():
            return ForEach(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), IntLiteral(int(ctx.INT_LIT().getText())), self.visitStatements_in_block(ctx.statements_in_block()))
        elif ctx.array_literal():
            return ForEach(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), self.visit(ctx.array_literal()), self.visitStatements_in_block(ctx.statements_in_block()))
        else:
            return ForEach(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), self.visitLhs(ctx.lhs()), self.visitStatements_in_block(ctx.statements_in_block()))


    # break_statement: BREAK;
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    # continue_statement: CONTINUE;
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()


    # call_statement: call_statement DOT call_statement | call_statement LBRACKET INT_LIT RBRACKET | call_statement_1;
    def visitCall_statement(self, ctx: MiniGoParser.Call_statementContext):
        if isinstance(ctx, list):
            if ctx[0].getChildCount() == 1:
                return self.visitCall_statement_1(ctx[0].call_statement_1())
            elif ctx[0].getChildCount() == 3:
                receiver = self.visitCall_statement(ctx[0].call_statement(0))
                member = self.visitCall_statement(ctx[0].call_statement(1))
                if isinstance(member, FuncCall):
                    return MethCall(receiver, member.funName, member.args)
                else:
                    return FieldAccess(receiver, member.name)
            else:
                receiver = self.visitCall_statement(ctx.call_statement())
                index = [IntLiteral(int(ctx.INT_LIT().getText(), 0))]
                return ArrayCell(receiver, index)
        else:
            if ctx.getChildCount() == 1:
                return self.visitCall_statement_1(ctx.call_statement_1())
            elif ctx.getChildCount() == 3:
                receiver = self.visitCall_statement(ctx.call_statement(0))
                member = self.visitCall_statement(ctx.call_statement(1))
                if isinstance(member, FuncCall):
                    return MethCall(receiver, member.funName, member.args)
                else:
                    return FieldAccess(receiver, member.name)
            else:
                receiver = self.visitCall_statement(ctx.call_statement())
                index = [IntLiteral(int(ctx.INT_LIT().getText(), 0))]
                return ArrayCell(receiver, index)


    # call_statement_1: ID | func_call;
    def visitCall_statement_1(self, ctx:MiniGoParser.Call_statement_1Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visitFunc_call(ctx.func_call())


    # return_statement: RETURN expression?;
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        if ctx.expression():
            return Return(self.visitExpression(ctx.expression()))
        else:
            return Return(None)