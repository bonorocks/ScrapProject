'''
Created on 22/05/2011

@author: Cassio
'''
import lxml.etree as ET

def trataArquivos():
    f = open("C:\Python27\PDFBox\Estrutura.txt")
    lines = f.readlines()
    root = ET.Element("root")
    line = ET.SubElement(root, "cargo")
    item1 = ET.SubElement(line, "nome")
    texto = ""
    padrao = ""
    cargo = ""
    muda = True
    for l in lines:  
     
      texto = l[0]+l[1]+l[2]
      if texto == "CON" or texto == "ANA":
          cargo = l
      
      if cargo == "CONSULTOR E ADVOGADO\n":  
          padrao = l[0]+l[1]    
          if padrao in ("45", "44", "43", "42", "41"):      
              elems = l.split("\n")
              elems = map(lambda x: x.strip(), elems)          
              item2 = ET.SubElement(line, "estrutura")
              item1.text = cargo
              item2.text = l
      else:
          if cargo == "ANALISTA LEGISLATIVO\n":
              if muda == True:
                  line = ET.SubElement(root, "cargo")
                  item1 = ET.SubElement(line, "nome")
                  muda = False      
              padrao = l[0]+l[1]    
              if padrao in ("45", "44", "43", "42", "41", "40", "39", "38", "37", "36"):              
                  elems = l.split("\n")
                  elems = map(lambda x: x.strip(), elems)          
                  item2 = ET.SubElement(line, "estrutura")
                  item1.text = cargo
                  item2.text = l
    
    tree = ET.ElementTree(root)
    tree.write("C:\Python27\PDFBox\Estrutura.xml", pretty_print=True)
