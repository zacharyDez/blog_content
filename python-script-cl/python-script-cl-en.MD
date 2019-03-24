# Adapter des scripts Python à la ligne de commande

## Pourquoi des scripts *.py* en ligne de commande?

- La simplicité de la ligne de commande

- La puissance de Python (Familiarité, niveau d'abstraction, lisibilité)

## Exécuter un script *.py* avec la ligne de commande

Tout script python peut-être exécuter à partir de la ligne de commande.

*saluer.py*
```python
nom = input('Enter name: ')

print(f'Hi {nom}!')     # f strings are awesome!
```
*Lire sur les [f-strings](https://docs.python.org/3/whatsnew/3.6.html)*

Pour exécuter le script:

```bash
$ python saluer.py
Enter name: Zac
Hi Zac!
```

Dans plusieurs cas, cette simple utilisation de la ligne de commande est suffisante.

## Additionner deux nombres ensembles

Dans cet exemple, on ne souhaite pas que le programme demande de saisir les nombres à additionner. 

On souhaite passer les deux nombres en arguments à la ligne de commande et qu'il soit exécuter immédiatement.

Les motivations sont au niveau de la vitesse de l'exécution et à la possibilité d'automatiser le traitement des chiffres à additionner dans des scripts plus imposants.

*Programme désiré:*
```bash
$ python add_together.py 56 90
146
```

Le module *sys* permet d'accéder aux arguments passé en ligne de commande:
```
import sys

# sys.argv[0] contient le nom du fichier

num_1 = float(sys.argv[1])
num_2 = float(sys.argv[2])

result = num_1 + num_2

print(result)
```

Remarque: Il est nécessaire de connaître les index des arguments passer en ligne de commande!
Comment pourrait-on additionner un nombre indéfini d'argument?

```
import sys

result = 0

# sys.argv[0] contient le nom du fichier
# cast les nombres de type str en int avec compréhension de liste
result = sum([int(num) for num in sys.argv[1:]])

print(result)
```

## Note convention du *main()*

Vous allez souvent voir la syntaxe suivante pour des scripts de ligne de commande. 

*gdal_calc.py* a justement cette syntaxe. 

```
import sys

def main(argv):
    # Votre code ici
    pass

if __name__ == "__main__":
    main(sys.argv)
```

L'objectif de la syntaxe est de pouvoir importer le fichier comme un module dans d'autres scripts 
et de pouvoir l'utiliser en ligne de commande aussi. 
C'est plus facile de tester le code et on peut l'importer dans le shell intéractif. 

[Explication détaillée](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

## Une ligne de commande avec des options

Jusqu'à présent, les scripts utiliser en ligne de commande utilise simplement *argv* pour les traitements.

Notre script d'addition de nombre était simple, mais exigeait que nous connaissons déjà sont utilisation. 
C'est-à-dire que la ligne de commande prenez autant de nombre passer en argument et faisait leur somme.

Une bonne pratique des lignes de commande est d'avoir une option d'aide (*-h*) qui explique comment utilisé la commande.
C'est ici que notre approche précédente ne fonctionne plus.

La limite de l'approche s'impose quand il est désiré d'avoir plus qu'une seule manière d'utilisé la commande. 
Que ce soit pour demandé de l'aide pour la commande ou de faire plusieurs traitements différents sur des *rasters* comme *gdal_calc.py*.
Ces scripts permettent de saisir les options et les arguments passés en ligne de commande 
et appel des procédures de traitement différents selon les options données.

Il y a plusieurs méthodes pour identifier les options et les arguments passés en ligne de commandes.
Quelques outils intéressants sont [*getopt*](https://docs.python.org/3/library/getopt.html) 
et [*argparse*](https://docs.python.org/3/library/argparse.html).

L'exemple présenté utilise *getopt*. La fonction *getopt* reçoit en arguments:
 1. Les arguments de la ligne de commande sans traitement (argv[1:])
 2. Les options (flags) à surveiller
    - Exemple de flag: *-h*
    - Les flags qui reçoivent des arguments sont suivis de *':'* dans la fonction
    - Exemple des options *help* (ne reçoit pas d'argument), *input* et *output*: _**'hi:o:'**_

Il est aussi possible de spécifier des *long_options*, des options ayant plus qu'un caractère.

Voici un exemple simple ayant les options d'aide, un fichier intrant et un fichier sortant. 
L'exemple peut être une référence pour des traitements plus avancés de fichiers.

*arg_parse_ex.py*
```
import getopt
import sys


def main(argv):
    # initialisé les fichiers input et output
    input_file = ''
    output_file = ''

    # Tenter de trouver les options et leur arguments
    try:
        opts, args = getopt.getopt(argv, "hi:o:")

    # imprimer l'utilisation de la commande si exception
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        # si option -h, imprimer utilisation de la commande
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()

        # Associé les options -i et -o aux fichiers input et output
        elif opt in ("-i"):
            input_file = arg

        elif opt in ("-o"):
            output_file = arg

    # Imprimer le nom des fichiers
    print('Fichier intrant:  "', input_file)
    print('Fichier sortant: "', output_file)


if __name__ == "__main__":
 # exclure le nom du fichier exécuter passé comme premier argument
    main(sys.argv[1:])
```

Un autre avantage de ces approches et que l'ordre des arguments n'est pas important. 
L'option *-i* peut être passé avant ou après l'option *-o*.

## Notre exemple d'addition de nombre avec une option *-h*:

*add_together.py*
```
import getopt
import sys

def main(argv):

    # Tenter de trouver les options et leur arguments
    try:
        opts, args = getopt.getopt(argv, "h")

    # imprimer l'utilisation de la commande si exception
    except getopt.GetoptError:
        print('python add_together <nombre_1> <nombre_2> ... <nombre_n>')
        sys.exit(2)

    for opt, arg in opts:
        # si option -h, imprimer utilisation de la commande
        if opt == '-h':
            print('python add_together <nombre_1> <nombre_2> ... <nombre_n>')
            sys.exit()  # important, autres traitements non-exécutés

    # somme des nombres
    result = sum([float(num) for num in argv])

    # Imprimer le nom des fichiers
    print('Somme des nombres: ', result)


if __name__ == "__main__":
    main(sys.argv[1:])
```

## Conclusion

Nous avons vu comment adapté des scripts Python pour la ligne de commande avec des niveaux de complexité différent.

Il y a des outils intéressant qui facilitent le développement d'outils de ligne de commande.

[click](https://click.palletsprojects.com/en/7.x/) est un package Python qui permet de développer des outils CLI avec le moins de code possible.

Pour un exemple concret d'utilisation en géomatique d'un script Python en ligne de commande, allez voir [Traitement d'image avec gdal_calc]().

# TODO: put urls

