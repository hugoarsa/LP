// Gramàtica per expressions aritmeriques senzilles
grammar lambda;
root : terme
     ;

terme: VAR                      #variable
     | '(' terme ')'            #termeParentitzat
     | LAMBDA vars DOT terme    #abstraccio
     | terme terme              #aplicacio
     ;

vars: (VAR)+;


DOT     : '.' ;
LAMBDA  : 'λ' | '\\' ;
VAR     : [a-z] ;
WS      : [ \t\n\r]+ -> skip ;