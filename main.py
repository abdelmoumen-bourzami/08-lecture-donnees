#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """Retourne le contenu du fichier <filename> sous forme de liste de listes d'entiers.

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 liste d'entiers par ligne)
    """
    with open(filename, mode="r", encoding="utf8") as f:
        lignes = f.readlines()
    # Chaque ligne est une chaîne -> on enlève le \n puis on split par ","
    data = [[int(x) for x in ligne.strip().split(";")] for ligne in lignes if ligne.strip()]
    return data


def get_list_k(data, k):
    """Retourne la k-ième liste de data."""
    return data[k]


def get_first(l):
    """Retourne le premier élément de la liste."""
    return l[0]


def get_last(l):
    """Retourne le dernier élément de la liste."""
    return l[-1]


def get_max(l):
    """Retourne le maximum de la liste."""
    return max(l)


def get_min(l):
    """Retourne le minimum de la liste."""
    return min(l)


def get_sum(l):
    """Retourne la somme des éléments de la liste."""
    return sum(l)


#### Fonction principale

def main():
    # Lecture des données
    data = read_data(FILENAME)

    # Affichage des 5 premières listes pour vérifier
    for i, l in enumerate(data[:5]):
        print(i, l)

    # Exemple avec une liste particulière
    k = 3
    lk = get_list_k(data, k)
    print(f"\nListe {k}:", lk)
    print("Premier élément:", get_first(lk))
    print("Dernier élément:", get_last(lk))
    print("Max:", get_max(lk))
    print("Min:", get_min(lk))
    print("Somme:", get_sum(lk))


if __name__ == "__main__":
    main()
