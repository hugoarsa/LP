// Gramàtica per expressions aritmeriques senzilles
grammar lambda;
root : terme
     ;

terme: '(' terme ')'               #termeParentitzat
     | terme terme                 #aplicacio
     | LAMBDA variables DOT terme  #abstraccio
     | VAR                         #variable
     ;

variables: VAR+;

VAR     : [a-z] ;



DOT     : '.' ;
LAMBDA  : 'λ' | '\\' ;
WS      : [ \t\n\r]+ -> skip ;