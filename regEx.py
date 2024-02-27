from regExVisitor import regExVisitor
import pandas as pd
import streamlit as st
from antlr4 import *
from regExLexer import regExLexer
from regExParser import regExParser


class regEx(regExVisitor):
    
    def __init__(self):
        self.ts = {}

    def visitRoot(self, ctx):
        L = list(ctx.getChildren())
        for i in L:
            self.visit(i)
        
        return self.ts["solution"]

    def visitOutput(self, ctx):
        [_, expr,_] = list(ctx.getChildren())
        leng1 = self.visit(expr)
        self.ts["solution"] = leng1
        

    def visitAsignacion(self, ctx):
        [id, _, expressio,_] = list(ctx.getChildren())
        self.ts[id.getText()] = self.visit(expressio)
    
    def visitUnion(self, ctx):
        [expressio1, _, expressio2] = list(ctx.getChildren())
        leng1 = self.visit(expressio1)
        leng2 = self.visit(expressio2)
        leng1.update(leng2)
        return leng1

    def visitResta(self, ctx):
        [expressio1, _, expressio2] = list(ctx.getChildren())
        leng1 = self.visit(expressio1)
        leng2 = self.visit(expressio2)
        for i in leng2:
            leng1.discard(i)
        return leng1

    def visitMot(self, ctx):
        [_, mot,_] = list(ctx.getChildren())
        leng1 = {mot.getText()}
        if len(mot.getText())<15:
            return leng1
        else:
            return set()
    
    def visitMotVacio(self,ctx):
        return {""}

    def visitLenguaje(self, ctx):
        [mot] = list(ctx.getChildren())
        return self.visit(mot)
    
    def visitIdVariable(self, ctx):
        [id] = list(ctx.getChildren())
        return self.ts[id.getText()]
    
    def visitParentesis(self,ctx):
        [_,expr,_] = list(ctx.getChildren())
        return self.visit(expr)
    

    def visitEstrella(self,ctx):
        [_,expr,_,_] = list(ctx.getChildren())
        leng1 = self.visit(expr)
        list2 = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2]
        mida = len(leng1)
        res= set()

        leng1lista = []
        for i in leng1:
            leng1lista.append(i)

        while (suma(list2, mida)):
            mot = ""
            for i in list2:
                if (i != -1):
                    mot += leng1lista[i]
            if (len(mot) < 15):
                res.add(mot)
        

        return res
    
    def visitConcatenacion(self, ctx):
        [expr1, expr2] = list(ctx.getChildren())
        leng1 = self.visit(expr1)
        leng2 = self.visit(expr2)
        res = set()
        for i in leng1:
            for j in leng2:
                if len(i+j)<15:
                    res.add(i+j)
        return res

    def visitSubstitucion(self, ctx):
        L = list(ctx.getChildren())
        [_,id] = L[0:2]
        leng1 = self.ts[id.getText()]
        self.subs = {}
        for i in L[2:(len(L)-1)]:
            self.visit(i)
        res = set()
        for i in leng1:
            mot = ""
            for j in i:
                if j in self.subs:
                    mot += self.subs[j]
                else:
                    mot += j
            if len(mot)<15:
                res.add(mot)
        self.ts[id.getText()] = res
    
    def visitSubstituto(self,ctx):
        L = list(ctx.getChildren())
        if (len(L) == 7):
            [_,CH,_,_,_,ID,_] = L
            self.subs[CH.getText()] = ID.getText()
        else:
            [_,CH,_,_,_,_] = L
            self.subs[CH.getText()] = ""


def suma(lista, mida):
    i = 13
    seguir = True
    while (i>=0 and seguir):
        seguir = False
        lista[i] +=1
        if (lista[i] >= mida):
            if (i == 0):
                return False
            seguir = True
            lista[i] = 0
        i -= 1
    return True

def visitaPrograma(nombre):
  input_stream = FileStream(nombre)
  lexer = regExLexer(input_stream)
  token_stream = CommonTokenStream(lexer)
  parser = regExParser(token_stream)
  tree = parser.root()
  if parser.getNumberOfSyntaxErrors() == 0:
      visitor = regEx()
      leng1 = visitor.visit(tree)
      return leng1
  else:
    print(parser.getNumberOfSyntaxErrors(), 'sintax errors.')
    print(tree.toStringTree(recog=parser))
  
def visitaProgramaInput(nombre):
  input_stream = InputStream(nombre)
  lexer = regExLexer(input_stream)
  token_stream = CommonTokenStream(lexer)
  parser = regExParser(token_stream)
  tree = parser.root()
  if parser.getNumberOfSyntaxErrors() == 0:
      visitor = regEx()
      leng1 = visitor.visit(tree)
      return leng1
  else:
    print(parser.getNumberOfSyntaxErrors(), 'sintax errors.')
    print(tree.toStringTree(recog=parser))

def comprobarSolucion(leng1,leng2):
  Correcto = True
  oldleng1 = leng1.copy()

  for i in leng2:
    leng1.discard(i)

  for i in leng1:
    Correcto = False
    st.write("Your language does not recognize the word: "+i)
    break

  for i in oldleng1:
    leng2.discard(i)

  for i in leng2:
    Correcto = False
    st.write("Your language should not contain the word: "+i)
    break

  if (Correcto):
    st.write("Your solution is correct")

def ejercicio(numero,enunciado,solucion):
  st.title("Exercise "+numero)
  st.text(enunciado)

  text = st.text_area("Write your solution: ", key='hola')
  if st.button("Submit"):
    leng1 = visitaPrograma(solucion)
    leng2 = visitaProgramaInput(text)
    comprobarSolucion(leng1,leng2)

  col1, col2 = st.columns([2, 1])

  text2 = col1.text_area("Write a word: ", key='hola2',height=80)
  col2.text("")
  col2.text("")
  if col2.button("Check if it is in your solution."):
    leng2 = visitaProgramaInput(text)
    if text2 in leng2:
      st.write("The word is in your solution.")
    else:
      st.write("The word is not in your solution.")

# Main del programa.
if __name__ == "__main__":
    text = st.text_area("Write the statement of the problem: ", key='hola3')
    text2 = st.text_area("Write the file that contains the solution (e.g. solution.txt) ", key='hola4')
    ejercicio("1",text,text2)
