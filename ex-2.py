#Exercice:
    #Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractère
    #Le caractère doit être parametable
#DEBUT
#Définir un la fonction par un argument
def miniGame(letterResult):
    #Attribuer une valeur d'input à n
    #Tant que la lettre H n'est pas renvoyée
    while input() != letterResult:
        print("Mauvaise lettre")
        #On donne à nouveau une valeur d'input à n
    #Retourne le resultat disant que n est égale à l'argument.
    return "Vous avez Gagnez"
print (miniGame("h"))

#FIN