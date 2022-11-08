#Exercice:
    #Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractère
    #Le caractère doit être parametable
#DEBUT
#Définir un la fonction par un argument
def miniGame(letterResult):
    #on met un compteur
    compteur = 1
    #Tant que la lettre H n'est pas renvoyée
    while input() != letterResult:
        compteur = compteur+1
        print("Mauvaise lettre")
        #On donne à nouveau une valeur d'input à n
    #Retourne le resultat disant que n est égale à l'argument.
    return "Vous avez Gagnez, après " +str(compteur)+" essaie(s)"
print (miniGame("h"))

#FIN

#DEBUT
#Définir un la fonction par un argument
def miniGame(letterResult):
    #Vérifier si la lettre est la bonne
    #Si le joueur à perduS
    if letterResult != input("Entrer une lettre"):
        #Afficher si le joueur à perdu
        print("Vous avez perdu")
        #Ajouter une valeur au compteur
        return miniGame(letterResult) + 1
    #Sinon le joueur  gagné
    else :
        print ("Vous avez gagnez")
        return 1 

print(miniGame("h"))
#FIN