// Gramàtica per expressions aritmeriques senzilles
grammar lc;
root : terme                                 
     | assignacio1                            
     ;

terme: '(' terme ')'                         #termeParentitzat
     | terme terme                           #aplicacio
     | ('λ' | '\\') variables DOT terme      #abstraccio
     | VAR                                   #variable
     | MACRO                                 #macro
     ;

variables: VAR+;

assignacio1: MACRO('=' | '≡')terme;

VAR     : [a-z] ;
MACRO   : [A-Z0-9]+ ;

DOT     : '.' ;
WS      : [ \t\n\r]+ -> skip ;