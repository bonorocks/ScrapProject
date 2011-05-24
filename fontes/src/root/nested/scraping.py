
'''Modulo principal.
'''
import scrapURL
import convertToXML

'''Funcao principal da aplicacao.
'''
def main():
   scrapURL.raspaURL()
   convertToXML.trataArquivos()

if __name__ == "__main__":
    main()
    