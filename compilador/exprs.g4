// Gramàtica per expressions senzilles
grammar exprs;
root : expr             // l'etiqueta ja és root
     ;

expr : <assoc=right> expr '^' expr    # expressioBinaria
     | expr '/' expr    # expressioBinaria
     | expr '*' expr    # expressioBinaria
     | expr '+' expr    # expressioBinaria
     | expr '-' expr    # expressioBinaria
     | NUM              # numero
     ;

//modificaciones para añadir en un futuro cosas
//assignacio : ID ':=' expr;

//write: 'write' ID;

NUM : [0-9]+ ;
//ID : [a-zA-Z]+ ;
WS  : [ \t\n\r]+ -> skip ;