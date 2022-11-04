def dirReduc(arr):
    #Liste de directions opposées
    opposites = ['NORTH SOUTH', 'SOUTH NORTH', 'EAST WEST', 'WEST EAST']
    #On boucle tant que la liste n'est pas vide
    while arr:
        #On convertit la liste en une chaîne de caractères
        arr_str = ' '.join(arr)
        #On boucle sur la liste des directions opposées
        for i in opposites:
            #Si on trouve une direction opposée, on la supprime de la liste
            if i in arr_str:
                arr_str = arr_str.replace(i, '')
                arr = arr_str.split()
                break
        #Si on n'a pas trouvé de direction opposée, on arrête la boucle
        else:
            break
    return arr