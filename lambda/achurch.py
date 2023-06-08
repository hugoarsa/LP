from __future__ import annotations
from dataclasses import dataclass

from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor

@dataclass
class Variable:
    name: str

@dataclass
class Abstraction:
    variable: str
    body: Term

@dataclass
class Application:
    function: Term
    argument: Term

Term = Variable | Abstraction | Application

class TreeVisitor(lcVisitor):
    def __init__(self):
        self.macros = {}

    def visitVariable(self, ctx):
        [var] = list(ctx.getChildren())
        return Variable(var.getText())

    def visitTermeParentitzat(self, ctx):
        [p1,ter,p2] = list(ctx.getChildren())
        return self.visit(ter)
    
    def visitMacroInfija(self, ctx):
        [terme1,ID,terme2] = list(ctx.getChildren())
        return Application(Application(self.macros[str(ID)],self.visit(terme1)),self.visit(terme2))

    def visitAbstraccio(self, ctx):
        [op1, vars, op2, terme] = list(ctx.getChildren())

        t = self.visit(terme)
        for c in reversed(self.visit(vars)):
            t = Abstraction(c, t)
        return t

    def visitVariables(self, ctx):
        vars = list(ctx.getChildren())
        return ''.join([var.getText() for var in vars])
    
    def visitMacro(self, ctx):
        [ID] = list(ctx.getChildren())
        return self.macros[str(ID)]

    def visitAplicacio(self, ctx):
        [function,argument] = list(ctx.getChildren())
        return Application(self.visit(function), self.visit(argument))

    def visitRoot(self, ctx):
        [terme] = list(ctx.getChildren())
        return self.visit(terme)
    
    def visitAssignacio1(self, ctx):  
        [m, eq, terme] = list (ctx.getChildren())
        self.macros[str(m)] = self.visit(terme)
        return 0
    
    def printMacros(self):
        for key, value in self.macros.items():
            print(key + " ≡ " + show(value))
    
def show(t: Term):
    match t:
        case Variable(name):
            return name
        case Abstraction(var,term):
            return "(" + "λ" + var + "." + show(term) + ")"
        case Application(function,argument):
            return "(" + show(function) + show(argument) + ")"
        
def evaluate_term(term: Term, max_reductions: int) -> Term:

    def substitute(term: Term, substitutions: dict) -> Term:
        match term:
            case Variable(name):
                if name in substitutions:
                    return substitutions[term.name]
                return term
            case Abstraction(variable,body):
                new_substitutions = {key: value for key, value in substitutions.items()}
                new_substitutions.pop(variable, None)
                new_body = substitute(body, new_substitutions)
                return Abstraction(variable, new_body)
            case Application(function,argument):
                new_function = substitute(function, substitutions)
                new_argument = substitute(argument, substitutions)
                return Application(new_function, new_argument)


    def evaluate_a_beta(term: Term) -> Term:

        match term:

            case Variable(var):
                return term, False
            
            case Abstraction(var,body):
                new_body, modif = evaluate_a_beta(body)
                return Abstraction(var, new_body), modif
            
            case Application(function,argument):

                if isinstance(term.function, Abstraction):

                    #aqui buscare las alfa conversiones necesarias

                    new_term = substitute(term.function.body, {term.function.variable: argument})
                    print("β-reducció:")
                    print(show(term) + " → " + show(new_term))

                    return new_term, True
                
                else:

                    new_function, modif = evaluate_a_beta(function)
                    if modif:
                        return Application(new_function, argument), modif

                    new_argument, modif = evaluate_a_beta(argument)
                    return Application(function, new_argument), modif
                
        return term
    
    
    for i in range(1,max_reductions):
        new_term, modif = evaluate_a_beta(term)
        if not modif:
            return new_term
        term = new_term
    
    #si llegamos aqui no hemos encontrado en los pasos el resultado
    return 0



visitor = TreeVisitor()
input_stream = InputStream(input('? '))
while input_stream:
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.root()

    expresion = visitor.visit(tree)

    if expresion != 0:
        # Escribe la expresion inicial con correcta parentizacion (tasca 2)
        print("Arbre: ")
        print(show(expresion))
        # print(expresion)

        # Evalua la expresion usando la estategia de orden de reduccón normal (tasca 3)
        evaluated_expression = evaluate_term(expresion, max_reductions=10)

        #escribe Nothing si este agota la cantidad de steps que ha de hacer
        print("Resultat: ")
        if evaluated_expression == expresion:
            print("Nothing")
        else:
            print(show(evaluated_expression))
    else:
        #ha sido una asignacion macro escribimos todas las macros (tasca 4)
        visitor.printMacros()


    input_stream = InputStream(input('? '))