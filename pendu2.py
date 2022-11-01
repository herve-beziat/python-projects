with open ("dico_france.txt", "r") as f:
    dico = f.read().split()
    import random
    chosen_word = (random.choice(dico))
    print(chosen_word)


crypted_word = ''
for i in range(len(chosen_word)):
        crypted_word += '-'
print(crypted_word)


level = input("Bonjour, à quel niveau souhaites-tu jouer? débutant, intermédiaire ou expert?\n")
remlife = 0
history = []

if level == "ez":
    remlife = 10
elif level == "intermédiaire":
    remlife = 7
elif level == "expert":
    remlife = 4
else:
    print("choix invalide")

index_of_letter = []

while remlife >= 0:
    if crypted_word == chosen_word:
        print("Gagné !")
        break
    if remlife == 0:
        print("Perdu !")
        break
    else:
        letter = input("Quelle lettre proposes-tu?")
        #letter_save = letter
        if letter in chosen_word:
            for i in range(len(chosen_word)):
                if letter == chosen_word[i]:
                    crypted_word = crypted_word[:i] + letter + crypted_word[i+1:]
            print(crypted_word)
            print("nombre de vies restantes: ", remlife)
            history.append(letter)
            if level != "expert":
                print("lettres proposées: ", history)
        else:
            remlife = remlife -1
            print("nombre de vies restantes: ", remlife)
            history.append(letter)
            if level != "expert":
                print("lettres proposées: ", history)
            print(crypted_word)
        

