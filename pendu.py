#ouverture du dictionnaire et intégration de la liste

import random
with open("dico_france.txt", "r") as dico:        
    contenu = dico.read().split()
    liste=list(contenu)
    solution=random.choice(liste)
    print(solution)


#définir input début de partie
lettres = []
life=0




print("Bienvenue dans le jeu du pendu.")
niveau = input("A quel niveau souhaites tu jouer? Débutant, Intermédiaire ou Expert : ")
life=0

if niveau == "Débutant":
    life=10
elif niveau == "Intermédiaire":
    life=7
elif niveau == "Expert":
    life=4
else:
    print("Choix invalide")
    life=0



cryptmot = ''
for i in range(len(solution)):
        cryptmot += '-'
print(cryptmot)
