#Exercie 1 
#Faire une fonction qui concatene 2 chaines de caractere, les séparants par une virgule
def concatWithComma(strA,strB):
    #Je m'assure que strA soit bien de type str
    stringifiedA= str(strA)
    #Je m'assure que strB soit bien de type str
    stringifiedB= str(strB)
    #Retourne strA +',' + strB
    return strA +','+ strB
concatWithComma(17, "épée")
#Exercice 2
#Faire une fonction qui itère sur tous les index d'un tableau renvoyant une chaine de caractere
#Avec l'ensemblres des occurences d'un chiffre e.g.:
#Pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau,0) doit renvoyer "0,4,7" n'hesitez pas à implementer la premiere fonction ,)
tableau=[0,1,1,1,0,1,1,0,1]
#Définir la fonction findIndex qui itère sur tableau, cherchant l'index des différentes occurences de x
def findIndex(tableau,x):
    #Définir un index de départ
    i = 0
    #Définir chaineRetour telle qu'une chaine de caractère vide
    chaineRetour= ""
    #Tant que i est différent du nombre d'elt dans le tableau 
    while (i != len(tableau)):
        #Alors j'attribue a une variable la valeur de tableau à l'index i
        selected = tableau[i]
        #Je définis un boolen tel que firstTurn est true
        firsTurn = True
        #Si selected est égale à x et que firstTurn est true 
        if selected == x and firsTurn == True :
            #Alors on asssigne à chaineRetour le retour de str(i)
            chaineRetour = str(i)
            #Changer la valeur de firstTurn à false
            firsTurn = False
        #Si selected est égale à x
        elif selected == x:
            #Alors j'assigne le retour de  concatWithComma tel que: concatWithComma (chainerRetour, i) à chaineRetour
            chaineRetour = concatWithComma(chaineRetour, i)
        #J'incrémente i de 1
        i= i + 1
    #Retourne la chaineRetour
    return chaineRetour
findIndex(tableau, 1)
#Exercice 3
#Renvoyer / Afficher un message

print("Afficher un message")