#### Imports et définition des variables globales
"""
Code permettant de lire des données
"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding= 'utf8')as f :
        return [list(map(int, line.strip().split(';'))) for line in f.readlines()]


def get_list_k(data, k):
    """
    fonction qui retourne la k-ième liste de donnée
    """
    return data[k]
def get_first(l):
    """
    Fonction qui retourne le 1er élément d'une liste
    """
    return l[0] if l else None

def get_last(l):
    """
    Fonction qui retourne le dernier élément d'une liste
    """
    return l[-1] if l else None

def get_max(l):
    """
    Fonction qui retourne le max élément d'une liste
    """
    return max(l) if l else None

def get_min(l):
    """
    Fonction qui retourne le min élément d'une liste
    """
    return min(l) if l else None

def get_sum(l):
    """
    Fonction qui retourne la somme des éléments d'une liste
    """
    return sum(l) if l else None


#### Fonction principale


def main():
    """ fonction principale qui test les fonctions secondaires
    """
   # "" data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #    print(i, l)
    #k = 37
    #print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
