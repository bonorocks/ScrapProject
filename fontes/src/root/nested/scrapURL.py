
import urllib
from subprocess import call

def raspaURL():
    urllib.urlretrieve ("http://www.senado.gov.br/transparencia/SECrh/QuadroPessoal_e_EstruturaRemuneratoria.pdf", "C:\Python27\PDFBox\Estrutura.pdf")
    call(['java', '-jar', 'C:\Python27\PDFBox\pdfbox-app-1.5.0.jar', 'ExtractText', '-force', '-startPage', '10', '-endPage', '10', 'C:\Python27\PDFBox\Estrutura.pdf', 'C:\Python27\PDFBox\Estrutura.txt'], shell=True)
