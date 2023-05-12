// Gramàtica per expressions aritmeriques senzilles
grammar exprs;
root : 
     | instruccio
     | expr             // l'etiqueta ja és root
     ;

instruccio : assignacio
           | condicional
           | write
           ;

assignacio : ID ':=' expr;

expr : <assoc=right> expr '^' expr    # ExpressioBinaria
     | expr '*' expr    # ExpressioBinaria
     | expr '/' expr    # ExpressioBinaria
     | expr '+' expr    # ExpressioBinaria
     | expr '-' expr    # ExpressioBinaria
     | NUM              # numero
     | ID               # variable
     ;

condicional : 'if' condicio 'then' instruccio 'end';

condicio : expr '=' expr      #igualtat
         | expr '<>' expr     #desigualtat
         ;

write: 'write' ID;

NUM : [0-9]+ ;
ID : [a-zA-Z]+ ;
WS  : [ \t\n\r]+ -> skip ;