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

prenom = "Gabriel"
nom = "Nang Ndong"
identite = nom + prenom #Retourne Nang NdongGabriel
identite = nom +''+ prenom #Retourne Nang Ndong Gabriel

integerValue = 342 #Retourne 342
stringIntegrerValue = str(342) #Retourne "342"

tableau = [0,10,15,5,1]
#Pour récupere 15 je prends dans tableau l'index 2

print(tableau[2]) #Affiche 15

len(tableau) #Renvoie la longueur de tableau renvoir 5

#Exercie 1 
#Faire une fonction qui concatene 2 chaines de caractere, les séparants par une virgule
def virgule(x,y):
    motPlusVirgule= x + ',' + '' + y
    print(motPlusVirgule)
    return
print("Gabriel", "Nang Ndong")

#Exercice 2
#Faire une fonction qui itère sur tous les index d'un tableau renvoyant une chaine de caractere
#Avec l'ensemblres des occurences d'un chiffre e.g.:
#Pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau,0) doit renvoyer "0,4,7" n'hesitez pas à implementer la premiere fonction ,)
tableau=[0,1,1,1,0,1,1,0,1]

def indexTableau(x):
    print(tableau(x))

indexTableau(1)
#Exercice 3
#Renvoyer / Afficher un message

print("Afficher un message")