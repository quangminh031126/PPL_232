from abc import ABC
from functools import reduce

from AST import *
from CodeGenError import *
from Emitter import Emitter
from Frame import Frame
from MachineCode import JasminCode
from Utils import *
from Visitor import *


# Since the Frame.py file is not submitted, have to do it here
def patch_Frame_class():
    def getBreakLabel(self):
        if not self.brkLabel:
            raise IllegalRuntimeException("None break label")
        return self.brkLabel[-1]

    Frame.getBreakLabel = getBreakLabel


# Since the MachineCode.py file is not submitted, have to do it here
def patch_Machine_Code_class():
    def emitIREM(self):
        return JasminCode.INDENT + "irem" + JasminCode.END

    JasminCode.emitIREM = emitIREM

    def emitFREM(self):
        return JasminCode.INDENT + "frem" + JasminCode.END

    JasminCode.emitFREM = emitFREM

    def emitICONST(self, i):
        # i: Int
        if i == -1:
            return JasminCode.INDENT + "iconst_m1" + JasminCode.END
        elif i >= 0 and i <= 5:
            return JasminCode.INDENT + "iconst_" + str(i) + JasminCode.END
        else:
            raise IllegalOperandException(str(i))

    JasminCode.emitICONST = emitICONST


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class MethodDecl:
    def __init__(self) -> None:
        pass


class Instance:
    def __init__(self) -> None:
        pass


class ClassType:
    def __init__(self) -> None:
        pass


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("readNumber", MType(list(), NumberType()), CName(self.libName)),
            Symbol(
                "writeNumber", MType([NumberType()], VoidType()), CName(self.libName)
            ),
            Symbol("readBool", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("readString", MType(list(), StringType()), CName(self.libName)),
            Symbol(
                "writeString", MType([StringType()], VoidType()), CName(self.libName)
            ),
        ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody:
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access:
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        patch_Frame_class()
        patch_Machine_Code_class()
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast, c):
        [self.visit(i, c) for i in ast.decl]
        return c

    def visitClassDecl(self, ast, c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        [
            self.visit(ele, SubBody(None, self.env))
            for ele in ast.memlist
            if type(ele) == MethodDecl
        ]
        # generate default constructor
        self.genMETHOD(
            MethodDecl(Instance(), Id("<init>"), list(), None, Block([], [])),
            c,
            Frame("<init>", VoidType()),
        )
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = (
            consdecl.name.name == "main"
            and len(consdecl.param) == 0
            and type(consdecl.returnType) is VoidType
        )
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = (
            [ArrayType(0, StringType())]
            if isMain
            else list(map(lambda x: x.typ, consdecl.param))
        )
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    "this",
                    ClassType(Id(self.className)),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame,
                )
            )
        elif isMain:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    "args",
                    ArrayType(0, StringType()),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame,
                )
            )
        else:
            local = reduce(
                lambda env, ele: SubBody(frame, [self.visit(ele, env)] + env.sym),
                consdecl.param,
                SubBody(frame, []),
            )
            glenv = local.sym + glenv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(
                self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame)
            )
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(
            ast.name,
            MType([x.typ for x in ast.param], ast.returnType),
            CName(self.className),
        )

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(
            self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
        )

    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), NumberType()

    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t
