import getopt
import sys


def main(argv):
    # initialisé les fichiers input et output
    input_file = ""
    output_file = ""

    # Tenter de trouver les options et leur arguments
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])

    # imprimer l'utilisation de la commande si exception
    except getopt.GetoptError:
        print("test.py -i <inputfile> -o <outputfile>")
        sys.exit(2)

    for opt, arg in opts:
        # si option -h, imprimer utilisation de la commande
        if opt == "-h":
            print("test.py -i <inputfile> -o <outputfile>")
            sys.exit()

        # Associé les options -i et -o aux fichiers input et output
        elif opt in ("-i", "--ifile"):
            input_file = arg

        elif opt in ("-o", "--ofile"):
            output_file = arg

    # Imprimer le nom des fichiers
    print('Input file is "', input_file)
    print('Output file is "', output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
