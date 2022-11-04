def order(sentence):
    #Cherche le nombre dans la phrase, ce nombre correspond à l'index de la liste words
    words = sentence.split()
    #Création d'une liste vide
    ordered = []
    #Pour chaque nombre de 1 à la longueur de la liste words
    for i in range(1, len(words)+1):
        #Pour chaque mot dans la liste words
        for word in words:
            #Si le nombre est dans le mot
            if str(i) in word:
                #Ajoute le mot à la liste ordered
                ordered.append(word)
    #Retourne la liste ordered
    return " ".join(ordered)