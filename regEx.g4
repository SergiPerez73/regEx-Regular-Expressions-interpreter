grammar regEx;
root : statement*           // l'etiqueta ja és root
     ;
statement : ID '=' expr ';' # asignacion
     | 'output' expr ';' #output
     | 'substitution ' ID '|' subs* ';' #substitucion
     ;

subs: '"' ID '"' '->' ('"' ID '"' | '"''"') #substituto
     ;

expr : expr ('+'|'|') expr # union
     | expr ('-') expr #resta
     | '(' expr ')' #parentesis
     | '(' expr ')' '*' #estrella
     | expr expr #concatenacion
     | leng # lenguaje
     ;

leng : ('"' ID '"') #mot
     | ('"' '"')  #motVacio
     | ID # idVariable
     ;

ID : [a-zA-Z0-9]+;

Numero : [0-9]+
     ;
     
WS  : [ \t\n\r]+ -> skip ;