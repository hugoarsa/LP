// Gramàtica per expressions aritmeriques senzilles
grammar lc;
root : terme
     ;

terme: '(' terme ')'                         #termeParentitzat
     | terme terme                           #aplicacio
     | ('λ' | '\\') variables DOT terme      #abstraccio
     | VAR                                   #variable
     ;

variables: VAR+;

VAR     : [a-z] ;



DOT     : '.' ;
//LAM     : 'λ' | '\\' ;
WS      : [ \t\n\r]+ -> skip ;