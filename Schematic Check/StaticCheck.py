from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple, Union

from StaticError import Type as StaticErrorType
from AST import Type

class FuntionType(Type):
    def __str__(self):
        return "FuntionType"

    def accept(self, v, param):
        return v.visitFuntionType(self, v, param)


class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value


    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor, Utils):
        
    def __init__(self, ast):
        self.ast = ast
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.list_function =  [
                FuncDecl("getInt", [], IntType(), Block([])),
                FuncDecl("putInt", [ParamDecl("param", IntType())], VoidType(), Block([])),
                FuncDecl("putIntLn", [ParamDecl("param", IntType())], VoidType(), Block([])),
                FuncDecl("getString", [], StringType(), Block([])),
                FuncDecl("putString", [ParamDecl("param", StringType())], VoidType(), Block([])),
                FuncDecl("putStringLn", [ParamDecl("param", StringType())], VoidType(), Block([])),
                FuncDecl("putLn",[],VoidType(),Block([Return(None)])),
                FuncDecl("putBool", [ParamDecl("param", BoolType())], VoidType(), Block([])),
                FuncDecl("getBool", [], BoolType(), Block([])),
                FuncDecl("putFloat", [ParamDecl("param", FloatType())], VoidType(), Block([])),
                FuncDecl("putFloatLn", [ParamDecl("param", FloatType())], VoidType(), Block([])),
            ]
        self.symbols = [
            Symbol("getInt", FuntionType()),
            Symbol("putInt", FuntionType()),
            Symbol("putIntLn", FuntionType()),
            Symbol("putString", FuntionType()),
            Symbol("getString", FuntionType()),
            Symbol("putStringLn", FuntionType()),
            Symbol("putLn", FuntionType()),
            Symbol("putBool", FuntionType()),
            Symbol("getBool", FuntionType()),
            Symbol("putFloat", FuntionType()),
            Symbol("putFloatLn", FuntionType()),
        ]

        self.function_current: FuncDecl = None
        self.list_struct: List[Tuple[str, List[str], List[str]]] = []

    def check(self):
        self.visit(self.ast, None)

    def checkType(self, LSH_type: Type, right_side_type: Type, list_type_permission: List[Tuple[Type, Type]] = []) -> bool:
        if isinstance(LSH_type, Id) and right_side_type.name == "":
            return True
        if type(LSH_type) == InterfaceType and right_side_type.name == "":
            return True
        if LSH_type == type(right_side_type) and right_side_type == IntType():
            return True
        
        # chuyển kiểu id về struct/interface nếu cần
        LSH_type = self.lookup(LSH_type.name, self.list_type, lambda x: x.name) if isinstance(LSH_type, Id) else LSH_type
        right_side_type = self.lookup(right_side_type.name, self.list_type, lambda x: x.name) if isinstance(right_side_type, Id) else right_side_type

        # so sánh array: số chiều và kiểu phần tử phải tương đương
        if isinstance(LSH_type, ArrayType) and isinstance(right_side_type, ArrayType):
            if self.checkType(LSH_type.eleType, right_side_type.eleType, list_type_permission):
                if len(LSH_type.dimens) == len(right_side_type.dimens):
                    # kiểm tra từng chiều, giá trị trong từng chiều phải bằng nhau
                    for i in range(len(LSH_type.dimens)):
                        if not self.evaluate_ast(LSH_type.dimens[i], [self.symbols]) == self.evaluate_ast(right_side_type.dimens[i], [self.symbols]):
                            return False
                    return True
                else:
                    return False
            else:
                return False
        # so sánh id với array: luôn đúng
        if isinstance(LSH_type, Id) and isinstance(right_side_type, ArrayType):
            return True

        # kiểm tra các cặp cho phép (float=int, interface=struct)
        if (type(LSH_type), type(right_side_type)) in list_type_permission:
            # nếu interface = struct thì kiểm tra các phương thức trong interface có được triển khai trong struct không
            if isinstance(LSH_type, InterfaceType) and isinstance(right_side_type, StructType):
                for proto in LSH_type.methods:
                    # tìm method trong struct có tên giống prototype
                    method = self.lookup(proto.name, right_side_type.methods, lambda x: x.fun.name)
                    if method is None:
                        return False
                    # kiểm tra số lượng tham số
                    if len(proto.params) != len(method.fun.params):
                        return False
                    # kiểm tra kiểu trả về và các tham số
                    if not self.checkType(method.fun.retType, proto.retType):
                        return False
                    for p_decl, p_proto in zip(method.fun.params, proto.params):
                        if not self.checkType(p_decl.parType, p_proto):
                            return False
                return True
            return True

        # so sánh cho struct/interface: so sánh theo tên
        if (isinstance(LSH_type, StructType) or isinstance(LSH_type, InterfaceType)) and \
           (isinstance(right_side_type, StructType) or isinstance(right_side_type, InterfaceType)):
            return LSH_type.name == right_side_type.name

        # so sánh kiểu bình thường: cùng loại
        return type(LSH_type) == type(right_side_type)

    def visitProgram(self, ast: Program, c: None):
        def visitMethodDecl(ast: MethodDecl, c: StructType) -> MethodDecl:
            if any(m.fun.name == ast.fun.name for m in c.methods) or \
            any(name == ast.fun.name for name, _ in c.elements):
                raise Redeclared(Method(), ast.fun.name)
            
            c.methods.append(ast)
            return ast
        
        
        list_str = ["getInt", "putInt", "putIntLn", "putString", "getString", "putStringLn", "putLn", "putBool", "getBool", "putFloat", "putFloatLn"]
        type_map = {
            VarDecl: lambda item: (item.varName, Variable()),
            ConstDecl: lambda item: (item.conName, Constant()),
            StructType: lambda item: (item.name, StaticErrorType()),
            InterfaceType: lambda item: (item.name, StaticErrorType())
        }

        for item in filter(lambda x: isinstance(x, tuple(type_map.keys())), ast.decl):
            name, error_type = type_map[type(item)](item)
            if name in list_str:
                raise Redeclared(error_type, name)
            list_str.append(name)




        # Kiểm tra method và field trong struct có trùng với nhau không?
        # for item in ast.decl:
        #     if isinstance(item, StructType):
        #         res = self.lookup(item.name, self.list_struct, lambda x: x[0])
        #         if res is None:
        #             list_field = []
        #             for ele in item.elements:
        #                 list_field.append(ele[0])
        #             self.list_struct.append((item.name, list_field, []))
        #         else:
        #             list_field = res[1]
        #             for ele in item.elements:
        #                 if ele[0] in res[2]:
        #                     raise Redeclared(Field(), ele[0])
        #                 list_field.append(ele[0])
        #     elif isinstance(item, MethodDecl):
        #         res = self.lookup(item.recType.name, self.list_struct, lambda x: x[0])
        #         if res is not None:
        #             if item.fun.name in res[1]:
        #                 raise Redeclared(Method(), item.fun.name)
        #             res[2].append(item.fun.name)
        #         else:
        #             self.list_struct.append((item.recType.name, [], [item.fun.name]))






        # Khởi tạo danh sách type và function
        self.list_type = [
            Symbol("getInt", FuntionType()),
            Symbol("putInt", FuntionType()),
            Symbol("putIntLn", FuntionType()),
            Symbol("putString", FuntionType()),
            Symbol("getString", FuntionType()),
            Symbol("putStringLn", FuntionType()),
            Symbol("putLn", FuntionType()),
            Symbol("putBool", FuntionType()),
            Symbol("getBool", FuntionType()),
            Symbol("putFloat", FuntionType()),
            Symbol("putFloatLn", FuntionType()),
        ]
        
        # Xử lý các Type
        types = filter(lambda ele: isinstance(ele, Type), ast.decl)
        self.list_type = list(map(lambda ele: self.visit(ele, self.list_type), types)) + self.list_type

        # Thêm các function vào danh sách
        self.list_function.extend(filter(lambda item: isinstance(item, FuncDecl), ast.decl))

        # Thêm function vào list_type để hỗ trợ kiểm tra kiểu
        self.list_type.extend(
            Symbol(item.name, FuntionType())
            for item in ast.decl if isinstance(item, FuncDecl)
        )

        # Xử lý các MethodDecl
        for item in filter(lambda item: isinstance(item, MethodDecl), ast.decl):
            struct_type = self.lookup(item.recType.name, self.list_type, lambda x: x.name)
            visitMethodDecl(item, struct_type)

        # Duyệt qua các khai báo và kiểm tra lỗi
        for ele in filter(lambda ele: isinstance(ele, Decl), ast.decl):
            result = self.visit(ele, [self.symbols])
            if isinstance(result, Symbol):
                self.symbols.insert(0, result)

    def visitStructType(self, ast: StructType, c : List[Union[StructType, InterfaceType]]) -> StructType:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if res is not None:
            raise Redeclared(StaticErrorType(), ast.name)
        def visitElements(element: Tuple[str,Type], elems: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            name, typ = element
            if any(name == n for n, _ in elems):
                raise Redeclared(Field(), name)
            return element

        ast.elements = reduce(lambda acc, ele: [visitElements(ele, acc)] + acc , ast.elements , [])
        return ast
    
    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        if any(proto.name == ast.name for proto in c):
            raise Redeclared(Prototype(), ast.name)
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c: List[Union[StructType, InterfaceType]]) -> InterfaceType:
        if any(item.name == ast.name for item in c):
            raise Redeclared(StaticErrorType(), ast.name)

        ast.methods = [self.visit(m, ast.methods[:i]) for i, m in enumerate(ast.methods)]
        return ast
    


    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]) -> Symbol:
        self.function_current = ast
        if self.lookup(ast.name, c[0], lambda x: x.name) is not None:
            raise Redeclared(Function(), ast.name)
                
        new_env = [list(reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.params, []))] + c
        self.visit(ast.body, new_env)
        return Symbol(ast.name, FuntionType())



    def visitParamDecl(self, ast: ParamDecl, c: List[Symbol]) -> Symbol:
        if any(sym.name == ast.parName for sym in c):
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]) -> None:
        receiver_env = [Symbol(ast.receiver, ast.recType)]  # Tạo môi trường riêng cho receiver
        param_env = []  # Môi trường riêng cho tham số
        
        for param in ast.fun.params:
            sym = self.visit(param, param_env)
            param_env.append(sym)
        
        combined_env = [param_env + receiver_env] + c
        
        temp = self.function_current
        self.function_current = ast.fun
        self.visit(ast.fun.body, combined_env)
        self.function_current = temp
        
    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        if any(sym.name == ast.varName for sym in c[0]):
            raise Redeclared(Variable(), ast.varName)

        left_type = ast.varType or None
        right_type = self.visit(ast.varInit, c) if ast.varInit else None

        if isinstance(ast.varInit, BinaryOp):
            if isinstance(left_type, IntType) and isinstance(right_type, FloatType):
                if ast.varInit.op in ['+', '-', '*', '/']:
                    raise TypeMismatch(ast)
            
            type_of_left = self.visit(ast.varInit, c)
            if isinstance(type_of_left, IntType) and ast.varInit.op in ['+', '-', '*']:
                value = self.evaluate_ast(ast.varInit, c)
                return Symbol(ast.varName, type_of_left, value)

        if isinstance(left_type, ArrayType) and isinstance(right_type, ArrayType):
            if isinstance(left_type.eleType, Id) and isinstance(right_type.eleType, Id):
                left = self.lookup(left_type.eleType.name, self.list_type, lambda x: x.name)
                right = self.lookup(right_type.eleType.name, self.list_type, lambda x: x.name)
                if isinstance(left, InterfaceType) and isinstance(right, StructType):
                    raise TypeMismatch(ast)

        if right_type is None:
            if isinstance(left_type, ArrayType):
                for i, dim in enumerate(left_type.dimens):
                    left_type.dimens[i] = IntLiteral(self.evaluate_ast(dim, c))
            return Symbol(ast.varName, left_type, None)

        if left_type is None:
            return Symbol(ast.varName, right_type, None)

        if self.checkType(left_type, right_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            return Symbol(ast.varName, left_type, None)

        if isinstance(ast.varInit, BinaryOp):
            raise TypeMismatch(ast.varInit)
        raise TypeMismatch(ast)

        

    def visitConstDecl(self, ast: ConstDecl, c: List[List[Symbol]]) -> Symbol:
        if any(sym.name == ast.conName for sym in c[0]):
            raise Redeclared(Constant(), ast.conName)

        if isinstance(ast.iniExpr, (BinaryOp, UnaryOp, IntLiteral)):
            expr_type = self.visit(ast.iniExpr, c)
            if isinstance(expr_type, IntType):
                value = self.evaluate_ast(ast.iniExpr, c)
                return Symbol(ast.conName, IntType, value)
            return Symbol(ast.conName, expr_type, None)

        expr_type = self.visit(ast.iniExpr, c) if ast.iniExpr else ast.conType
        return Symbol(ast.conName, expr_type, None)



    def _eval_binary_op(self, node: BinaryOp, c: List[List[Symbol]]) -> int:
        left = self.evaluate_ast(node.left, c)
        right = self.evaluate_ast(node.right, c)

        ops = {
            '+': lambda l, r: l + r,
            '-': lambda l, r: l - r,
            '*': lambda l, r: l * r,
            '/': lambda l, r: l // r if r != 0 else self._div_zero_error(),
            '%': lambda l, r: l % r if r != 0 else self._mod_zero_error(),
        }

        if node.op in ops:
            return ops[node.op](left, right)

        raise StaticError(f"Unsupported binary operator: {node.op}")

    def _eval_unary_op(self, node: UnaryOp, c: List[List[Symbol]]) -> int:
        val = self.evaluate_ast(node.body, c)
        if node.op == '-':
            return -val
        raise StaticError(f"Unsupported unary operator: {node.op}")

    def _div_zero_error(self):
        raise StaticError("Division by zero")

    def _mod_zero_error(self):
        raise StaticError("Modulo by zero")

    def evaluate_ast(self, node: AST, c: List[List[Symbol]]) -> int:
        if isinstance(node, IntLiteral):
            return int(node.value)

        if isinstance(node, Id):
            res = next((x for scope in reversed(c) for x in scope if x.name == node.name), None)
            if res and isinstance(res.value, int):
                return res.value
            raise StaticError(f"Cannot resolve identifier: {node.name}")

        if isinstance(node, BinaryOp):
            return self._eval_binary_op(node, c)

        if isinstance(node, UnaryOp):
            return self._eval_unary_op(node, c)

        raise StaticError(f"Cannot evaluate AST node: {type(node).__name__}")

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        acc = [[]] + c  # tạo scope mới

        for ele in ast.member:
            result = self.visit(ele, (acc, True)) if isinstance(ele, (FuncCall, MethCall)) else self.visit(ele, acc)
            
            if isinstance(result, Symbol):  # chỉ var/const mới thêm vào scope
                acc[0].insert(0, result)
                  
    def visitForBasic(self, ast: ForBasic, c: List[List[Symbol]]) -> None:
        self.assert_bool_condition(ast.cond, c, ast)
        self.visit(ast.loop, c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        init_symbol = self.visit(ast.init, [[]] + c)

        self.assert_bool_condition(ast.cond, [[init_symbol]], ast)

        loop_block = Block([ast.init, ast.upda] + ast.loop.member)
        self.visit(loop_block, c)

    def assert_bool_condition(self, cond_expr, c, node):
        cond_type = self.visit(cond_expr, c)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(node)
    
    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        type_array = self.visit(ast.arr, c)
        if not isinstance(type_array, ArrayType):
            raise TypeMismatch(ast)
        type_idx = self.visit(ast.idx, c)
        res = next((x for scope in c for x in scope if x.name == ast.idx.name), None)
        if res is None:
            raise Undeclared(Type(), ast.idx.name)
        if not self.checkType(type_idx, IntType()):
            raise TypeMismatch(ast)
        type_value = self.visit(ast.value, c)
        # Giảm một chiều của mảng
        if isinstance(type_array, ArrayType):
            if len(type_array.dimens) > 1:
                reduced_array = ArrayType(type_array.dimens[1:], type_array.eleType)
            else:
                reduced_array = type_array.eleType  # Nếu chỉ còn 1 chiều thì eleType là kiểu phần tử
        else:
            raise TypeMismatch(ast)
        if not self.checkType(type_value, reduced_array):
            raise TypeMismatch(ast)

        self.visit(Block(ast.loop.member), c)
    
    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:  
        res = next((x for scope in c for x in scope if x.name == ast.name), None)
        
        if not res or isinstance(res.mtype, Function):
            raise Undeclared(Identifier(), ast.name)

        return self.resolve_type(res.mtype, ast)

    def resolve_type(self, mtype, ast: Id) -> Type:
        if isinstance(mtype, Id):
            typ = self.lookup(mtype.name, self.list_type, lambda x: x.name)
            if typ is None:
                raise Undeclared(Type(), mtype.name)
            return typ
        return mtype
    



    def visitFuncCall(self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c
        list_arg = c[0]
        if len(c) > 1:
            list_arg += c[1]
        list_arg += c[-1]
        res = self.lookup(ast.funName, list_arg, lambda x: x.name)
        if res is not None and not isinstance(res.mtype, FuntionType):
            raise Undeclared(Function(), ast.funName)
        
        res = self.lookup(ast.funName, self.list_function, lambda x: x.name)

        if res:
            if len(res.params) != len(ast.args):
                raise TypeMismatch(ast)
            for param, arg in zip(res.params, ast.args):
                argType = self.visit(arg, list(c))
                if not self.checkType(param.parType, argType):
                    raise TypeMismatch(ast)
                
            if is_stmt and not isinstance(res.retType, VoidType):
                raise TypeMismatch(ast)
            if not is_stmt and isinstance(res.retType, VoidType):
                raise TypeMismatch(ast)
            return res.retType
        raise Undeclared(Function(), ast.funName)

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        receiver_type = self.visit(ast.receiver, c)
        # nếu receiver_type là Id thì tìm kiếm trong list_type
        if isinstance(receiver_type, Id):
            receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name)
        # yêu cầu receiver phải là StructType (không bao gồm interface)
        if not isinstance(receiver_type, StructType):
            raise TypeMismatch(ast)
        
        res = self.lookup(ast.field, receiver_type.elements, lambda x: x[0])
        if res is None:
            raise Undeclared(Field(), ast.field)
        return res[1]

    def visitMethCall(self, ast: MethCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c
        receiver_type = self.visit(ast.receiver, c)
        if isinstance(receiver_type, Id):
            receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name)
        if not (isinstance(receiver_type, StructType) or isinstance(receiver_type, InterfaceType)):
            raise TypeMismatch(ast)
        res = None
        if isinstance(receiver_type, StructType):
            res = self.lookup(ast.metName, receiver_type.methods, lambda x: x.fun.name)
            if res:
                if len(res.fun.params) != len(ast.args):
                    raise TypeMismatch(ast)
                for param, arg in zip(res.fun.params, ast.args):
                    argType = self.visit(arg, c)
                    if not self.checkType(param.parType, argType):
                        raise TypeMismatch(ast)
                if is_stmt and not isinstance(res.fun.retType, VoidType):
                    raise TypeMismatch(ast)
                if not is_stmt and isinstance(res.fun.retType, VoidType):
                    raise TypeMismatch(ast)   
                return res.fun.retType
        elif isinstance(receiver_type, InterfaceType):
            res = self.lookup(ast.metName, receiver_type.methods, lambda x: x.name)
            if res:
                if len(res.params) != len(ast.args):
                    raise TypeMismatch(ast)
                for param, arg in zip(res.params, ast.args):
                    argType = self.visit(arg, c)
                    if not self.checkType(param, argType):
                        raise TypeMismatch(ast)
                if is_stmt and not isinstance(res.retType, VoidType):
                    raise TypeMismatch(ast)
                if not is_stmt and isinstance(res.retType, VoidType):
                    raise TypeMismatch(ast)   
                return res.retType
        raise Undeclared(Method(), ast.metName)
        

    def visitIntType(self, ast, c: List[List[Symbol]]) -> Type: 
        return ast

    def visitFloatType(self, ast, c: List[List[Symbol]])-> Type: 
        return ast

    def visitBoolType(self, ast, c: List[List[Symbol]])-> Type: 
        return ast

    def visitStringType(self, ast, c: List[List[Symbol]]) -> Type: 
        return ast

    def visitVoidType(self, ast, c: List[List[Symbol]]) -> Type: 
        return ast

    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]):
        for dim in ast.dimens:
            if not isinstance(self.visit(dim, c), IntType):
                raise TypeMismatch(ast)
        return ast

    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) -> None:
        if type(ast.lhs) is Id:
            # TÌM KIẾM XEM BIẾN ĐÃ ĐƯỢC KHAI BÁO CHƯA, NẾU CHƯA ĐƯỢC KHAI BÁO THÌ TRẢ VỀ Symbol(ast.lhs.name, self.visit(ast.rhs, c), None)
            res = next((x for scope in c for x in [self.lookup(ast.lhs.name, scope, lambda y: y.name)] if x is not None), None)
            if res is None:
                sym = Symbol(ast.lhs.name, self.visit(ast.rhs, c), None)
                c[0] = [sym] + c[0]
        left_side_type = self.visit(ast.lhs, c)
        right_side_type = self.visit(ast.rhs, c)
        if not self.checkType(left_side_type, right_side_type, [(FloatType, IntType), (InterfaceType, StructType), (StructType, InterfaceType), (Id, IntType)]):
            raise TypeMismatch(ast)
        
        
    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None: 
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(Block(ast.thenStmt.member), c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)

    def visitContinue(self, ast, c: List[List[Symbol]]) -> None: 
        return None

    def visitBreak(self, ast, c: List[List[Symbol]]) -> None: 
        return None

    def visitReturn(self, ast, c: List[List[Symbol]]) -> None: 
        if self.function_current is None:
            return None
        expected = self.function_current.retType
        actual = self.visit(ast.expr, c) if ast.expr is not None else VoidType()
        if not self.checkType(expected, actual):
            raise TypeMismatch(ast)
        return None

    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
        left_side_type = self.visit(ast.left, c)
        right_side_type = self.visit(ast.right, c)
        
        if ast.op in ['+']:
            if self.checkType(left_side_type, right_side_type, [(IntType, FloatType), (FloatType, IntType)]):
                if isinstance(left_side_type, StringType):
                    return StringType()
                elif isinstance(left_side_type, FloatType) or isinstance(right_side_type, FloatType):
                    return FloatType()
                elif isinstance(left_side_type, IntType):
                    return IntType()
                return IntType() # Why <class 'AST.IntType'> different with IntType()?
        elif ast.op in ['-', '*', '/']:
            if self.checkType(left_side_type, right_side_type, [(IntType, FloatType), (FloatType, IntType)]):
                if isinstance(left_side_type, FloatType) or isinstance(right_side_type, FloatType):
                    return FloatType()
                else:
                    return IntType()
        elif ast.op in ['%']:
            if isinstance(left_side_type, IntType) and isinstance(right_side_type, IntType):
                return IntType()
        elif ast.op in ['&&', '||']:
            if isinstance(left_side_type, BoolType) and isinstance(right_side_type, BoolType):
                return BoolType()
        elif ast.op in ['==','!=','<','<=','>','>=']:
            if self.checkType(left_side_type, right_side_type, []) or (type(left_side_type)==type(right_side_type)):
                return BoolType()
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        unary_type = self.visit(ast.body, c)

        if isinstance(unary_type, type) and unary_type == IntType:
            unary_type = unary_type()  # Create an instance of IntType

        if ast.op == '-':
            if isinstance(unary_type, IntType) or isinstance(unary_type, FloatType):
                return unary_type
            elif isinstance(unary_type, Id):
                res = self.lookup(ast.body.name, self.list_type, lambda x: x.name)
                
                if res is None:
                    raise Undeclared(Type(), unary_type.name)
                if isinstance(res, IntType) or isinstance(res, FloatType):
                    return res
                else:
                    raise TypeMismatch(ast)
            else:
                raise TypeMismatch(ast)
        elif ast.op == '!':
            if isinstance(unary_type, BoolType):
                return BoolType()
            else:
                raise TypeMismatch(ast)
        else:
            raise TypeMismatch(ast)
    
    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        array_type = self.visit(ast.arr, c)
        if not isinstance(array_type, ArrayType):
            raise TypeMismatch(ast)
       
        if not all(self.checkType(self.visit(item, c), IntType()) for item in ast.idx):
            raise TypeMismatch(ast)
        if len(array_type.dimens) == len(ast.idx):
            return array_type.eleType
        elif len(array_type.dimens) > len(ast.idx):
            return ArrayType(array_type.dimens[len(ast.idx):], array_type.eleType)
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast, c: List[List[Symbol]]) -> Type: 
        return IntType()

    def visitFloatLiteral(self, ast, c: List[List[Symbol]]) -> Type: 
        return FloatType()

    def visitBooleanLiteral(self, ast, c: List[List[Symbol]]) -> Type: 
        return BoolType()

    def visitStringLiteral(self, ast, c: List[List[Symbol]]) -> Type: 
        return StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral , c: List[List[Symbol]]) -> Type:  
        def nested2recursive(dat: Union[Literal, list['NestedList']], c: List[List[Symbol]]):
            if isinstance(dat, list):
                list(map(lambda value: nested2recursive(value, c), dat))
            else:
                self.visit(dat, c)
        nested2recursive(ast.value, c)
        return ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast: StructLiteral, c: List[List[Symbol]]) -> Type: 
        list(map(lambda value: self.visit(value[1], c), ast.elements))
        res = self.lookup(ast.name, self.list_type, lambda x: x.name)
        if res is None:
            raise Undeclared(Type(), ast.name)
        return res

    def visitNilLiteral(self, ast: NilLiteral, c: List[List[Symbol]]) -> Type: 
        return StructType("", [], [])
