import os

directory = "/Users/jonathanturetta/Google Drive/Estudos (em uso)/Curso | Python | Angela/Aulas/"


def createFolder(dirName):
    i = 1
    for i in range (17,100):
        if not os.path.exists(
            f'/Users/jonathanturetta/Google Drive/Estudos (em uso)/Curso | Python | Angela/Aulas/{dirName}{i}'
        ):
            os.makedirs(
                f'/Users/jonathanturetta/Google Drive/Estudos (em uso)/Curso | Python | Angela/Aulas/{dirName}{i}'
            )
            print("Folder ", dirName + str(i),  " Created ")
            i += 1


createFolder('Day ')
