# import module
from pdf2image import convert_from_path
import sys

def getArgs():
# store pdf with convert_from_path function

fileName = sys.argv[1]
pngName = fileName[0:fileName.index(".")]

images = convert_from_path(fileName, size=300)   
        
images[0].save(pngName+ '.png', 'PNG')

