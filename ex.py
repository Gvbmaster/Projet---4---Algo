#DEBUT
#ex 1
from pickle import FALSE


assertionFinal = (((365 * 3) / (24 - (16 - 8))) * (230) > 12000) == (10 * 1250 < 12000)
pta= (((365 * 3) / (24 - (16 - 8))) * (230) > 12000) 
#15740.625 > 12000  
#true
ptb= (10 * 1250 < 12000) 
#12500 < 12000
#false
ptfinal = pta == ptb #false
#ex2
assertionFinalDeux = (((365 * 3) / (4 - (12 - 8))) * (230) > 12000) == (10 * 1250 < 12000)
pta = (((365 * 3) / (4 - (12 - 8))) * (230) > 12000) 
#false
ptb = (10 * 1250 < 12000)
#false
ptfinaldeux = FALSE == FA #true
def retournerSixPlusTrois ():
    return 6 + 3
def retournerYPlusX (x):
    return 6 + x
#ECRIRE "BONJOUR MONDE"
#PRINT " HELLO WORLD"
#retournerSixPlusTrois()
#retournerSixPlusX(9)
print("Hello World !")

#exos

#DEBUT
def add(x,y):
    return x + y
#FIN
#DEBUT
def sub(x,y):
    return x - y
#FIN
#DEBUT
def multiply(x,y):
    return x * y
#FIN
#DEBUT
#Definir une fonction qui divise x par y et retourner le resultat
def divide(x,y):
        #Si y est egale a 0
            if y == 0:
        #Alors écrire un message d'erreur
        print("ERROR : Cannot divide by 0")
        #Retourner vide
    return x / y
#FIN
#DEBUT
def modulo(x,y):
    return x % y
#FIN
#DEBUT
def salaireNet(Brut, coefficient)
    return Brut * coefficient
#FIN
#DEBUT
def salaireParSeconde(salaireHoraire,heureParJourOuvre,jourOuvreParAn):
    #Caluler mon salaire annuel
    salaireAnnuel = salaireHoraire * heureParJourOuvre * jourOuvreParAns
    #Calculer le nombre de secondes dans une année
    nbSecondesParAns = 365*24*60*60
    #Je pose et retourne la division
    return salaireAnnuel / nbSecondesParAns

#Défnir une fonciton withdrawFees qui retire un pourcentage à un total en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
    #Défninir Fees en fonction d'un total et d'un pourcentage 
    fees= total * (percent/100)
    #soustraire fees à un total
    result = total - fees
    #retourner la valeur obtenue
    return result

#Définir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteure d'activité (isPublic > booleen)
def calculBrutEnNet(salaireBrut, isPublic):
    #Si je suis un travailleur du secteur public
    if isPublic: 
        #Alors je soustrais 15% de mon salaire Brut à mon salaire brut et je l'assigne à la variable salaireNet
        #salaireNet = salaireBrut - (salaireBrut * 15 / 100)
        salaireNet = withdrawFees(salaireBrut, 15)
    #Sinon : Je suis un travailleur du secteur privé
    else:
        #Alors je soustrais 23% de mon salaire Brut à mon salaire brut et je l'assigne à la variable salaireNet
        #salaireNet = salaireBrut - (salaireBrut * 23 / 100)
        salaireNet = withdrawFees(salaireBrut, 23)
    #Retourner le salaireNet
    return salaireNet
#FIN
def input():
    #Renvoie un caractère de type string au hasard