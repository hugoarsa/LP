// Gramàtica per expressions aritmeriques senzilles
grammar exprs;
root : instruccions
     ;

instruccions : instruccio*
             ;

instruccio
     : assignacio
     | condicional
     | bucle
     | write
     ;

assignacio : ID ':=' expr;

write: 'write' expr;

condicio : expr '=' expr      #igualtat
         | expr '<>' expr     #desigualtat
         ;

condicional : 'if' condicio 'then' instruccions 'end';

bucle : 'while' condicio 'do' instruccions 'end';

expr : <assoc=right> expr '^' expr    # ExpressioBinaria
     | expr '*' expr    # ExpressioBinaria
     | expr '/' expr    # ExpressioBinaria
     | expr '+' expr    # ExpressioBinaria
     | expr '-' expr    # ExpressioBinaria
     | NUM              # numero
     | ID               # variable
     ;

NUM : [0-9]+ ;
ID : [a-zA-Z]+ ;
WS  : [ \t\n\r]+ -> skip ;