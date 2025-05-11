import unittest
from TestUtils import TestChecker
from AST import *
import inspect

class CheckSuite(unittest.TestCase):
    def test_001(self):
        """
var VoTien = 1; 
var VoTien = 2;
        """
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien", inspect.stack()[0].function))

    def test_002(self):
        """
var VoTien = 1; 
const VoTien = 2;
        """
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),ConstDecl("VoTien",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: VoTien", inspect.stack()[0].function))

    def test_003(self):
        """
const VoTien = 1; 
var VoTien = 2;
        """
        input = Program([ConstDecl("VoTien",None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien", inspect.stack()[0].function))

    def test_004(self):
        """
const VoTien = 1; 
func VoTien () {return;}
        """
        input = Program([ConstDecl("VoTien",None,IntLiteral(1)),FuncDecl("VoTien",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: VoTien", inspect.stack()[0].function))

    def test_005(self):
        """ 
func VoTien () {return;}
var VoTien = 1;
        """
        input = Program([FuncDecl("VoTien",[],VoidType(),Block([Return(None)])),VarDecl("VoTien", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien", inspect.stack()[0].function))

    def test_006(self):
        """ 
var getInt = 1;
        """
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getInt", inspect.stack()[0].function))

    def test_007(self):
        """ 
type Votien struct {
    Votien int;
}
type TIEN struct {
    Votien string;
    TIEN int;
    TIEN float;
}
        """
        input = Program([StructType("Votien",[("Votien",IntType())],[]),StructType("TIEN",[("Votien",StringType()),("TIEN",IntType()),("TIEN",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: TIEN", inspect.stack()[0].function))

    def test_008(self):
        """ 
func (v TIEN) putIntLn () {return;}
func (v TIEN) getInt () {return;}
func (v TIEN) getInt () {return;}
type TIEN struct {
    Votien int;
}
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))), StructType("TIEN",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt", inspect.stack()[0].function))

    def test_009(self):
        """ 
type VoTien interface {
    VoTien ();
    VoTien (a int);
}
        """
        input = Program([InterfaceType("VoTien",[Prototype("VoTien",[],VoidType()),Prototype("VoTien",[IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: VoTien", inspect.stack()[0].function))

    def test_010(self):
        """ 
func Votien (a, a int) {return;}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a", inspect.stack()[0].function))

    def test_011(self):
        """ 
func Votien (b int) {
    var b = 1;
    var a = 1;
    const a = 1;
}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_012(self):
        """ 
func Votien (b int) {
    for var a = 1; a < 1; a += 1 {
        const a = 2;
    }
}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_013(self):
        """ 
var a = 1;
var b = a;
var c = d;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d", inspect.stack()[0].function))

    def test_014(self):
        """ 
func Votien () int {return 1;}

fun foo () {
    var b = Votien();
    foo_votine();
    return;
}
        """
        input = Program([FuncDecl("Votien",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("Votien",[])),FuncCall("foo_votine",[]),Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_votine", inspect.stack()[0].function))

    def test_015(self):
        """ 
type TIEN struct {
    Votien int;
}

func (v TIEN) getInt () {
    const c = v.Votien;
    var d = v.tien;
}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"Votien")),VarDecl("d", None,FieldAccess(Id("v"),"tien"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: tien", inspect.stack()[0].function))

    def test_016(self):
        """ 
type TIEN struct {
    Votien int;
}

func (v TIEN) getInt () {
    v.getInt ();
    v.putInt ();
}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: putInt", inspect.stack()[0].function))

    def test_024(self):
        """
type TIEN struct {a int;}
type VO struct {a int;}
type TIEN interface {foo();}
        """
        input = Program([StructType("TIEN",[("a",IntType())],[]),StructType("VO",[("a",IntType())],[]),InterfaceType("TIEN",[Prototype("foo",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: TIEN", inspect.stack()[0].function))

    def test_028(self):
        """
        type TIEN interface {
            foo();
        }
        func TIEN() {return;}
        func foo() {return;}
        func TIEN() {return;}
        """
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType())]),FuncDecl("TIEN",[],VoidType(),Block([Return(None)])),FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("TIEN",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: TIEN", inspect.stack()[0].function))

    def test_030(self):
        """
func putInt () {return;}
        """
        input = Program([FuncDecl("putInt",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putInt", inspect.stack()[0].function))

    def test_032(self):
        """
func getString() {return;}
        """
        input = Program([FuncDecl("getString",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: getString", inspect.stack()[0].function))

    def test_038(self):
        """
        const a = 1;
        func foo() {
            var a = 1;
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_044(self):
        """ 
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) foo (v int) {return;}
        func foo () {return;}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_046(self):
        """
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) foo (a, b int) {return;}
        func foo (a, a int) {return;}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a", inspect.stack()[0].function))

    def test_051(self):
        """
        const a = 2;
        func foo () {
            const a = 1;
            for var a = 1; a < 1; b := 2 {
                const b = 1;
        """
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("b"),IntLiteral(2)),Block([ConstDecl("b",None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: b", inspect.stack()[0].function))

    def test_053(self):
        """
func foo () {
    var a = 1;
    var b = 1;
    for a, b := range [3]int {1, 2, 3} {
        var b = 1;
    }
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",None,IntLiteral(1)),VarDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_060(self):
        """
        var a = d;
        func foo () {
            const b = 1;
            for a, c := range [3]int{1, 2, 3} {
                var d = c;
            }
        }
        """
        input = Program([VarDecl("a", None,Id("d")),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("c"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("c"))])),VarDecl("d", None,Id("a")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("a"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d", inspect.stack()[0].function))

    def test_061(self):
        """
    var a = foo();
    func foo () int {
        var a = koo();
        var c = getInt();
        putInt(c);
        putIntLn(c);
        return 1;
    }
    var d = foo();
    func koo () int {
        var a =  foo ();
        return 1;
    }
        """
        input = Program([VarDecl("a", None,FuncCall("foo",[])),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,FuncCall("koo",[])),VarDecl("c", None,FuncCall("getInt",[])),FuncCall("putInt",[Id("c")]),FuncCall("putIntLn",[Id("c")]),Return(IntLiteral(1))])),VarDecl("d", None,FuncCall("foo",[])),FuncDecl("koo",[],IntType(),Block([VarDecl("a", None,FuncCall("foo",[])),Return(IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_065(self):
        """
    var v TIEN;
    const b = v.b;        
    type TIEN struct {
        a int;
        b int;
        c int;
    }
    const a = v.a;
    const e = v.e;
        """
        input = Program([VarDecl("v",Id("TIEN"), None),ConstDecl("b",None,FieldAccess(Id("v"),"b")),StructType("TIEN",[("a",IntType()),("b",IntType()),("c",IntType())],[]),ConstDecl("a",None,FieldAccess(Id("v"),"a")),ConstDecl("e",None,FieldAccess(Id("v"),"e"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: e", inspect.stack()[0].function))

    def test_072(self):
        """
        var v int = 1.02;
        """
        input = Program([VarDecl("v",IntType(),FloatLiteral(1.02))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(\"v\",IntType(),FloatLiteral(1.02))", inspect.stack()[0].function))

    def test_078(self):
        """
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien();}
        type I2 interface {votien();}

        func (s S1) votien() {return;}

        var a S1;
        var b S2;
        var c I1 = a;
        var d I2 = b;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),InterfaceType("I2",[Prototype("votien",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("b"))])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: votien""", inspect.stack()[0].function))

    def test_081(self):
        """
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien(e, e int) S1;}
        type I2 interface {votien(a int) S1;}

        func (s S1) votien(a, b int) S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("votien",[IntType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("votien",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a"))])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: votien""", inspect.stack()[0].function))

    def test_085(self):
        """
        func foo(){
            var v int;
            const x = v;
            var k float = x;
            var y boolean = x;
        }

        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("v",IntType(), None),ConstDecl("x",None,Id("v")),VarDecl("k",FloatType(),Id("x")),VarDecl("y",BoolType(),Id("x"))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(\"y\",BoolType(),Id(\"x\"))", inspect.stack()[0].function))
    def test_091(self):
        """
        type TIEN struct {v int;}
        var v TIEN;
        func foo(){
            for 1 {
                var a int = 1.2;
            }
        }
        """
        input = Program([StructType("TIEN",[("v",IntType())],[]),VarDecl("v",Id("TIEN"), None),FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ForBasic(IntLiteral(1),Block([VarDecl(\"a\",IntType(),FloatLiteral(1.2))]))", inspect.stack()[0].function))

    def test_096(self):
        """
        var a = [2] int {1, 2}
        var c [2] float = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(2)],FloatType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_102(self):
        """
        var a = [2][3] int
        var b = a[1]
        var c [2] int = b
        var d [1] string = b
        """
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(2)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(\"c\",ArrayType([IntLiteral(2)],IntType()),Id(\"b\"))", inspect.stack()[0].function))

    def test_107(self):
        """
        type S1 struct {votien int;}
        type I1 interface {votien();}
        var a I1;
        var c I1 = nil;
        var d S1 = nil;
        func foo(){
            c := a;
            a := nil;
        }

        var e int = nil;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),VarDecl("a",Id("I1"), None),VarDecl("c",Id("I1"),NilLiteral()),VarDecl("d",Id("S1"),NilLiteral()),FuncDecl("foo",[],VoidType(),Block([Assign(Id("c"),Id("a")),Assign(Id("a"),NilLiteral())])),VarDecl("e",IntType(),NilLiteral())])

        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(\"e\",IntType(),NilLiteral())", inspect.stack()[0].function))

    def test_111(self):
        """
        var a = 1 + 2.0;
        var b = 1 + 1;
        func foo() int {
            return b;
            return a;
        }
        """
        input = Program([VarDecl("a", None,BinaryOp("+", IntLiteral(1), FloatLiteral(2.0))),VarDecl("b", None,BinaryOp("+", IntLiteral(1), IntLiteral(1))),FuncDecl("foo",[],IntType(),Block([Return(Id("b")),Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(Id("a"))""", inspect.stack()[0].function))

    def test_113(self):
        input = Program([VarDecl("a",FloatType(),BinaryOp("*", IntLiteral(1), FloatLiteral(2.0))),VarDecl("b",IntType(),BinaryOp("/", IntLiteral(1), IntLiteral(2))),VarDecl("c",FloatType(),BinaryOp("/", IntLiteral(1), IntLiteral(2))),FuncDecl("foo",[],IntType(),Block([Return(Id("b")),Return(Id("c"))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(Id("c"))""", inspect.stack()[0].function))

    def test_115(self):
        """
        var a int = 1 % 2;
        var b int = 1 % 2.0;
        """
        input = Program([VarDecl("a",IntType(),BinaryOp("%", IntLiteral(1), IntLiteral(2))),VarDecl("b",IntType(),BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(\"%\", IntLiteral(1), FloatLiteral(2.0))", inspect.stack()[0].function))
                                               
    def test_117(self):
        """
        var a boolean = 1 > 2;
        var b boolean = 1.0 < 2.0;
        var c boolean = "1" == "2";
        var d boolean = 1 > 2.0;
        """
        input = Program([
            VarDecl("a",BoolType(),BinaryOp(">", IntLiteral(1), IntLiteral(2))),
            VarDecl("b",BoolType(),BinaryOp("<", FloatLiteral(1.0), FloatLiteral(2.0))),
            VarDecl("c",BoolType(),BinaryOp("==", StringLiteral('1'), StringLiteral('2'))),
            VarDecl("d",BoolType(),BinaryOp(">", IntLiteral(1), FloatLiteral(2.0)))
            ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(\">\", IntLiteral(1), FloatLiteral(2.0))", inspect.stack()[0].function))

    def test_121(self):
        """
        func foo(){
            for var i int = 1; a ! 10; i := 1. {
                var a = 1;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("i"),FloatLiteral(1.)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a", inspect.stack()[0].function))

    def test_122(self):
        """
        func foo(){
            for var i int = 1; i; i := 1. {
                var a = 1;
            }
        }    
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),Id("i"),Assign(Id("i"),FloatLiteral(1.)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ForStep(VarDecl(\"i\",IntType(),IntLiteral(1)),Id(\"i\"),Assign(Id(\"i\"),FloatLiteral(1.0)),Block([VarDecl(\"a\", None,IntLiteral(1))]))", inspect.stack()[0].function))

    def test_126(self):
        """
        func foo(){
            var arr [2][3] int;
            var a = 1;
            var b[3]int;
            for a, b := range arr {
                var c int = a;
                var d [3]int = b;
                var e [2]string = a;
            }
        } 
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("a", None,IntLiteral(1)),VarDecl("b",ArrayType([IntLiteral(3)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("e",ArrayType([IntLiteral(2)],StringType()),Id("a"))]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl("e",ArrayType([IntLiteral(2)],StringType()),Id("a"))""", inspect.stack()[0].function))                                                 

    def test_136(self):
        """
        func foo() int {return 1;}
        func votien() int {
            return votien();
            foo();
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("votien",[],IntType(),Block([Return(FuncCall("votien",[])),FuncCall("foo",[])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(\"foo\",[])", inspect.stack()[0].function))
    
    def test_139(self):
        """
        type Person struct {
            name string ;
            age int ;
        }

        func votien()  {
            var person = Person{name: "Alice", age: 30}
            person.name := "John";
            person.age := 30;
            putStringLn(person.name)
            putStringLn(person.Greet())
        }

        func (p Person) Greet() string {
            return "Hello, " + p.name
        }        
        """
        input = Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),
                         FuncDecl("votien",[],VoidType(),Block([VarDecl("person", None,StructLiteral("Person",[("name",StringLiteral("Alice")),("age",IntLiteral(30))])),Assign(FieldAccess(Id("person"),"name"),StringLiteral("John")),Assign(FieldAccess(Id("person"),"age"),IntLiteral(30)),FuncCall("putStringLn",[FieldAccess(Id("person"),"name")]),FuncCall("putStringLn",[MethCall(Id("person"),"Greet",[])])])),MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([Return(BinaryOp("+", StringLiteral("Hello, "), FieldAccess(Id("p"),"name")))])))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_140(self):
        """
        var a string;
        func foo() {
            var a int = 2;
            putIntLn(a);
        }
        """
        input = Program([VarDecl("a",StringType(), None),FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(2)),FuncCall("putIntLn",[Id("a")])]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_143(self):
        """
        var a TIEN;
        func foo() TIEN {
            return a;
            return TIEN;
        }

        type TIEN struct {tien int;}
        """
        input = Program([VarDecl("a",Id("TIEN"), None),FuncDecl("foo",[],Id("TIEN"),Block([Return(Id("a")),Return(Id("TIEN"))])),StructType("TIEN",[("tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: TIEN""", inspect.stack()[0].function)) 















    def test_149(self):
        """
        func putLn() {return ;}
        """
        input = Program([FuncDecl("putLn",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putLn", inspect.stack()[0].function))

    def test_151(self):
        """
        type putLn struct {a int;};
        """
        input = Program([StructType("putLn",[("a",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: putLn", inspect.stack()[0].function))

    def test_153(self):
        """
        var a int = getBool();
        """
        input = Program([VarDecl("a",IntType(),FuncCall("getBool",[]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(\"a\",IntType(),FuncCall(\"getBool\",[]))", inspect.stack()[0].function))

    def test_154(self):
        """
        func foo() {
            putFloat(getInt());
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putFloat",[FuncCall("getInt",[])])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(\"putFloat\",[FuncCall(\"getInt\",[])])", inspect.stack()[0].function))

    def test_165(self):
        """
        type TIEN struct {a [2]int;} 

        func foo() TIEN {
            return nil
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),FuncDecl("foo",[],Id("TIEN"),Block([Return(NilLiteral())]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_168(self):
        """
        func foo() {
            var a int = 2.0 * 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(),BinaryOp("*", FloatLiteral(2.0), IntLiteral(1)))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(\"a\",IntType(),BinaryOp(\"*\", FloatLiteral(2.0), IntLiteral(1)))", inspect.stack()[0].function))

    def test_174(self):
        """
        var A = 1;
        type A struct {a int;}
        """
        input = Program([VarDecl("A", None,IntLiteral(1)),StructType("A",[("a",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: A", inspect.stack()[0].function))

    def test_176(self):
        """
    type A interface {foo();}
    const A = 2;
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),ConstDecl("A",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, """Redeclared Constant: A""", inspect.stack()[0].function)) 

    def test_181(self):
            """
    func foo(a [2] float) {
        foo([2] float {1.0,2.0})
        foo([2] int {1,2})
    }
            """
            input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],FloatType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])]),FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])]))])
            self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])""", inspect.stack()[0].function)) 

    def test_182(self):
        """
        type S1 struct {votien int;}
        type I1 interface {votien();}

        func (s S1) votien() {return;}

        var b [2] S1;
        var a [2] I1 = b;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)]))),VarDecl("b",ArrayType([IntLiteral(2)],Id("S1")), None),VarDecl("a",ArrayType([IntLiteral(2)],Id("I1")),Id("b"))])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: votien""", inspect.stack()[0].function)) 

    def test_184(self):
        """
        var a [1 + 9] int;
        var b [10] int = a;
        """
        input = Program([VarDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(9))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(10)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, """VOTIEN""", inspect.stack()[0].function)) 

    def test_190(self):
        """
const v = 3;
const a = v + v;
var b [a * 2 + a] int;
var c [18] int = b;
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("v"), Id("v"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(18)],IntType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, """VOTIEN""", inspect.stack()[0].function)) 

    def test_191(self):
        """
        const v = 3;
        var c [3] int = [v * 1] int {1, 2, 3}; 
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),ArrayLiteral([BinaryOp("*", Id("v"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestChecker.test(input, """VOTIEN""", inspect.stack()[0].function))

    def test_196(self):
        """
        const a = "2" + "#";
        const b = a * 5;
        """
        input = Program([ConstDecl("a",None,BinaryOp("+", StringLiteral("2"), StringLiteral("#"))),ConstDecl("b",None,BinaryOp("*", Id("a"), IntLiteral(5)))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp("*", Id("a"), IntLiteral(5))""", inspect.stack()[0].function))                                                                          

    def test_197(self):
        """
        var v = 2 * 3;
        const a = v + 1;
        const b = a * 5;
        const c = ! (b > 3);
        """
        input = Program([VarDecl("v", None,BinaryOp("*", IntLiteral(2), IntLiteral(3))),ConstDecl("a",None,BinaryOp("+", Id("v"), IntLiteral(1))),ConstDecl("b",None,BinaryOp("*", Id("a"), IntLiteral(5))),ConstDecl("c",None,UnaryOp("!",BinaryOp(">", Id("b"), IntLiteral(3))))])
        self.assertTrue(TestChecker.test(input, """VOTIEN""", inspect.stack()[0].function))

    def test_199(self):
        """
        const a = 3;
        const b = -a;
        const c = -b;
        var d [c] int = [3] int {1,2,3}
        """
        input = Program([ConstDecl("a",None,IntLiteral(3)),ConstDecl("b",None,UnaryOp("-",Id("a"))),ConstDecl("c",None,UnaryOp("-",Id("b"))),VarDecl("d",ArrayType([Id("c")],IntType()),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestChecker.test(input, """VOTIEN""", inspect.stack()[0].function))

    def test_202(self):
        """
        func foo() {
            a := 1;
            var a = 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: a""", inspect.stack()[0].function))

    def test_208(self):
        """
        func Votien (b int) {
            for var a = 1; c < 1; a += c {
                const c = 2;
            }
        }
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), Id("c"))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: c""", inspect.stack()[0].function)) 

    def test_210(self):
        """
        var v TIEN;
        func (v TIEN) foo (v int) int {
            return v;
        }

        type TIEN struct {
            Votien int;
        }
        """
        input = Program([VarDecl("v",Id("TIEN"), None),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],IntType(),Block([Return(Id("v"))]))),StructType("TIEN",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_211(self):
        """
        var a int;
        func (v TIEN) foo () int {
            return a;
            return v;
        }
        type TIEN struct {
            Votien int;
        }
        """
        input = Program([VarDecl("a",IntType(), None),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(Id("a")),Return(Id("v"))]))),StructType("TIEN",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(Id("v"))""", inspect.stack()[0].function))

    def test_216(self):
        """
        func (v TIEN) VO () {return ;}
        func (v TIEN) Tien () {return ;}
        type TIEN struct {
            Votien int;
            Tien int;
        }
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType()),("Tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: Tien""", inspect.stack()[0].function))

    def test_221(self):
        """
        var a = 1;
        func foo() {
            a := 3;
            var a = 1.0
            for var a = 1; a > 1; a := 1 {
                return
            }
        }
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(3)),VarDecl("a", None,FloatLiteral(1.0)),ForStep(VarDecl("b", None,IntLiteral(1)),BinaryOp(">", Id("b"), IntLiteral(1)),Assign(Id("b"),IntLiteral(1)),Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input, """VOTIEN""", inspect.stack()[0].function))

    def test_228(self):
        input = """
        func foo() int {
            const foo = 1;
            return foo()
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo""", inspect.stack()[0].function))

    def test_239(self):
        """
        var v TIEN;      
        type TIEN struct {
            a int;
        } 
        type VO interface {
            fooA();
            fooB();
            fooC();
        }

        func (v TIEN) fooA() {return ;}
        func (foo TIEN) fooB() {
            foo()
            return;
        }
        func (v TIEN) fooC()  {return ;}

        func foo() {
            var x VO = TIEN{a:1};  
        }
        """
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[]),InterfaceType("VO",[Prototype("fooA",[],VoidType()),Prototype("fooB",[],VoidType()),Prototype("fooC",[],VoidType())]),MethodDecl("v",Id("TIEN"),FuncDecl("fooA",[],VoidType(),Block([Return(None)]))),MethodDecl("foo",Id("TIEN"),FuncDecl("fooB",[],VoidType(),Block([FuncCall("foo",[]),Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("fooC",[],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("VO"),StructLiteral("TIEN",[("a",IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo""", inspect.stack()[0].function))

    def test_240(self):
        """
        var v TIEN;      
        type TIEN struct {
            a int;
        } 
        type VO interface {
            fooA();
            fooB();
            fooC();
        }

        func (v TIEN) fooA() {return ;}
        func (foo TIEN) fooB() {
            return ;
        }
        func (v TIEN) fooC()  {return ;}

        func foo(foo int) {
            var x VO = TIEN{a:1}; 
            foo()
        }       
        """
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[]),InterfaceType("VO",[Prototype("fooA",[],VoidType()),Prototype("fooB",[],VoidType()),Prototype("fooC",[],VoidType())]),MethodDecl("v",Id("TIEN"),FuncDecl("fooA",[],VoidType(),Block([Return(None)]))),MethodDecl("foo",Id("TIEN"),FuncDecl("fooB",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("fooC",[],VoidType(),Block([Return(None)]))),FuncDecl("foo",[ParamDecl("foo",IntType())],VoidType(),Block([VarDecl("x",Id("VO"),StructLiteral("TIEN",[("a",IntLiteral(1))])),FuncCall("foo",[])]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo""", inspect.stack()[0].function))

    def test_241(self):
        """
        func Votien (b int) {
            var array = [2] int {1,2}
            var index = 1.0;
            var value int;

            for index, value := range  array {
                return;
            }
        }
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("array", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("index", None,FloatLiteral(1.0)),VarDecl("value",IntType(), None),ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))""", inspect.stack()[0].function))

    def test_245(self):
        """
        func Votien () {
            var array [2][3] int;
            var index int;
            var value [3] int;
            for index, value := range array {
                var value [2] int;
                for index, value := range array {
                    return
                }
            }
        }
        """
        input = Program([FuncDecl("Votien",[],VoidType(),Block([VarDecl("array",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("index",IntType(), None),VarDecl("value",ArrayType([IntLiteral(3)],IntType()), None),ForEach(Id("index"),Id("value"),Id("array"),Block([VarDecl("value",ArrayType([IntLiteral(2)],IntType()), None),ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))""", inspect.stack()[0].function))