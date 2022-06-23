import os

directory = "/Users/jonathanturetta/Google Drive/Estudos (em uso)/Curso | Python | Angela/Aulas/"

def createFolder(dirName): 
    i = 1
    while i <= 100:
        if not os.path.exists('/Users/jonathanturetta/Google Drive/Estudos (em uso)/Curso | Python | Angela/Aulas/' + dirName + str(i)):
            os.makedirs('/Users/jonathanturetta/Google Drive/Estudos (em uso)/Curso | Python | Angela/Aulas/' + dirName + str(i))
            print("Folder " , dirName + str(i) ,  " Created ") 
            i += 1

createFolder('Day ')
