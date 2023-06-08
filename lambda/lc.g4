// Gramàtica per expressions aritmeriques senzilles
grammar lc;
root : terme                                 
     | assignacio1                            
     ;

terme: '(' terme ')'                         #termeParentitzat
     | terme INMACRO terme                   #macroInfija
     | terme terme                           #aplicacio
     | ('λ' | '\\') variables DOT terme      #abstraccio
     | VAR                                   #variable
     | MACRO                                 #macro
     ;

variables: VAR+;

assignacio1: (MACRO|INMACRO) ('=' | '≡') terme;

VAR     : [a-z] ;
MACRO   : [A-Z0-9]+ ;
INMACRO : [\-+*/] ;

DOT     : '.' ;
WS      : [ \t\n\r]+ -> skip ;