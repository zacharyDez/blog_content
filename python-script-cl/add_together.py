import getopt
import sys


def main(argv):

    # Tenter de trouver les options et leur arguments
    try:
        opts, args = getopt.getopt(argv, "h")

    # imprimer l'utilisation de la commande si exception
    except getopt.GetoptError:
        print("python add_together <nombre_1> <nombre_2> ... <nombre_n>")
        sys.exit(2)

    for opt, arg in opts:
        # si option -h, imprimer utilisation de la commande
        if opt == "-h":
            print("python add_together <nombre_1> <nombre_2> ... <nombre_n>")
            sys.exit()  # important, quit la session

    # somme des nombres
    result = sum([float(num) for num in argv])

    # Imprimer le nom des fichiers
    print("Somme des nombres: ", result)


if __name__ == "__main__":
    main(sys.argv[1:])
