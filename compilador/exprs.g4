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

NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;