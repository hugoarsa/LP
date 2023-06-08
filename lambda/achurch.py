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
    def beta_reduction(term: Term) -> Term:
        if isinstance(term, Application) and isinstance(term.function, Abstraction):
            abstraction = term.function
            argument = term.argument

            #creo que aqui tendria que añadir una clase de funcion que haga 
            #check for alpha conversions antes de substituir para ver si
            #la substitucion genera conflictos y entonces renombrar

            new_term = substitute(abstraction.body, {abstraction.variable: argument})

            print("β-reducció:")
            print(show(term) + " → " + show(new_term))
            return new_term
        return term

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


    def evaluate_recursive(term: Term, reductions: int) -> Term:
        if reductions <= 0:
            return term

        term = beta_reduction(term)

        match term:
            case Abstraction(var,body):
                new_body = evaluate_recursive(body, reductions - 1)
                if new_body != body:
                    return evaluate_recursive(Abstraction(var, new_body), reductions - 1)
            case Application(function,argument):
                new_function = evaluate_recursive(function, reductions - 1)
                new_argument = evaluate_recursive(argument, reductions - 1)

                if new_function != function or new_argument != argument:
                    return evaluate_recursive(Application(new_function, new_argument), reductions - 1)
                
        return term
    
    return evaluate_recursive(term, max_reductions)



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

        # Evalua la expresion usando la estategia de orden de reduccón normal (tasca 3)
        evaluated_expression = evaluate_term(expresion, max_reductions=100)

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