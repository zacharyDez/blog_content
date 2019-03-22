# Introduction au shell et à la ligne de commande

Contenu initalement publié sur [mon site](zacharydeziel.com).

## Source du contenu

La source du contenu suit l'approche développé par [Software Carpentry](https://software-carpentry.org/) 
dont l'objectif est d'équiper des chercheurs avec les outils technologiques d'aujourd'hui. 
L'ensemble du contenu de leurs leçons est Open Source. 

Je remercie les contributeurs de l'organisation.

Référence au bas du document. 


## Obtenir les données

Le fichier compressé des données est disponible [ici](https://software-carpentry.org/).
## Cheat Sheet

L'objectif du document est de servir comme référence après l'atelier d'introduction.

## Introduction au Shell

##### Question

> - C'est quoi la ligne de commande et pourquoi je devrais l'utiliser?

##### Objectifs:
> - Comprendre les liens entre les usagers et l'ordinateur
> - Comprendre quand et pourquoi les lignes de commandes sont plus adaptées que des interfaces graphiques

#### Contexte

À un haut-niveau les ordinateurs peuvent:
- Exécuter un program
- Stocker des des données
- Communiquer entre eux
- Intéragir avec des usagers

Ils peuvent faire ses tâches de plusieurs méthodes différentes par l'entremise du clavier, d'une souris, d'un écran tactile ou même par reconnaissance de la voix.

Nous sommes tous familiers avec des interfaces graphiques (GUI) qui consiste en des fenêtres, des icons et des pointeurs. 
Ils sont faciles à apprendre et excellent pour exécuter des tâches simples. 
Ils permettent avec un usager, peu importe ses connaissances informatiques, d'exécuter une tâche.
Cette magie dépend de plusieurs petites tâches simples and d'avoir accès à des programmes qui font ces tâches simples.
 
Si vous désirez accomplir des tâches plus complexes et appliquer à un domaine spécifique, avoir des connaissances du shell sont nécessaires pour communiquer avec l'ordinateur.
La connaissance de simple commandes permettent d'automatiser une grande charge de travail.

Le coeur d'une interface de ligne de commande est la relation lecture-évaluation-sortie (*read-evaluate-print, REPL* ). 
Quand une commande est saisie, elle est évaluer et ensuite une sortie (résultat) est imprimée.

## Définition du Shell

Le Shell est un programme qui utilise d'autres programmes pour exécuter les calculs au lieu de les effectuer lui même. 
Il y a plusieurs Shell qui existe. 
Bash est le shell par défaut des systèmes d'opérations Unix and de plusieurs extensions du Shell sur Windows.

Python a un shell intéractif qui utilise le même principe: le shell appel l'interpréteur Python pour faire les calculs.
C'est un outil important pour expérimenter avec des solutions potentiels pour des programmes. 
Très utilisé pour l'exploration de jeux de donnés.

![Exemple Shell](img/ex-cl-ls.png)

## Comment que le Shell comprend les commandes and ces arguments?

Chaque commande à un programme qui est stocké sur l'ordinateur et le shell possède une liste des endroits où chercher 
pour les commandes (dans la fameuse variable PATH).

#### Logic du Shell:
1. Lire la commande saisie (séparation par espace et **';'** entre les commandes)
2. Évaluer la commande:
    - Trouver le programme de la commande
    - Exécuter la commande en y passant les arguments
3. Imprimer la sortie de la commande.

Si la commande n'est pas trouvée, des messages d'erreurs seront imprimées comme sortie.

#### Différence avec un GUI

Un GUI vous présente des options et vous êtes limités par ces options.
Avec une ligne de commande, il est possible d'établir des combinaisons plus adapté à un contexte précis.

#### Flexibilité et automatisation

Le shell permet de prendre des commandes existantes et de développer des pipelines de traitement plus avancés.
Cette capacité est fondamentale pour traiter des grands volumes de données. 
Il est possible d'écrire des séquences de commandes dans des scripts pour avoir des méthodes reproductibles.


## Naviguer des dossiers et des fichiers

#### Questions
> - Comment se déplacer sur notre ordinateur?
> - Comment connaître les fichiers sur mon ordinateur?
> - Comment spécifier l'emplacement d'un dossier ou d'un fichier sur mon ordinateur?

#### Objectifs
> - Expliquer les similarités et les différences entre un dossier et un fichier.
> - Traduire un path absolue en path relatif et vice-versa
> - Construire des paths qui identify des fichiers ou dossiers spécifique.

La partie du système d'opération (OS) qui s'occupe de la gestion de fichier se nomme le système de fichier. 
Il organise nos données en fichiers ou en dossier. 
Les fichiers ont de l'information, tandis que les dossiers sont composés de fichiers ou de d'autres dossiers.

Plusieurs commandes existent pour créer, inspecter, renommer et supprimer des fichiers ou dossiers.

## Commandes de navigation du système de fichiers

#### Notes différences de systèmes d'opérations

Les machines windows séparent les dossiers par **'\\'** et les machines Unix par **'/'**. 

Certaines commandes peuvent ne pas être disponibles dans le shell de votre machine. 

Le PowerShell est une bonne option sur Windows: [alias commandes Unix](https://docs.microsoft.com/en-us/powershell/scripting/learn/using-familiar-command-names?view=powershell-6).

#### Imprimer le répertoire de travail (print working directory)
```bash
    $ pwd
```

```bash
    /Users/zac
```

#### Lister les contenus d'un dossier

```bash
    $ ls -F
```

Le flag -F permet de savoir quel type de contenu est lister (à l'aide du symbole **'/'**)

```bash
    python-exception-handling-intro/ shell-cl-intro/
```

#### Obtenir de l'aide pour une commande

Obtenir le manuel de la commande: chercher unix man page.

```bash
    $ man ls
```

Les manuels sont disponibles en ligne aussi.

## TODO: check if works on windows

Obtenir de l'aide :
```bash
    $ ls --help
```

#### Outils intéressant de ls

Présenter tous les dossiers et fichiers de façon récursive:
```bash
    $ ls -R
```

Présenter les dossiers et fichiers par date de modification:
```bash
    $ ls -t
```

Présenter les dossiers et fichiers d'un autre dossier:
```bash
    $ ls -F Desktop
```

#### Outils externes

Sur mac (brew doit être installé): 

```bash
$ brew install tree
```

```bash
    $ tree
```

```bash
.
├── python-exception-handling-intro
│   ├── generate_password.py
│   ├── generer_mot_passe.py
│   └── python-exception-handling-intro.MD
└── shell-cl-intro
    └── shell-cl-intro-en.MD
```

#### Naviguer à un dossier

```bash
    $ cd Desktop
```

#### Remonter d'un dossier

```bash
    $ cd ..
```

Présenter les dossiers parents cachés:
```bash
    $ ls -F -a
```

#### Le tilde: '~'

Le **~** est interpréter comme référence au dossier mère de l'usager (home directory).

```bash
    $ cd ~/Desktop
```

Le tilde reconstruit un path non-relatif vers le dossier mère à partir de l'emplacement énoncé.

#### Absolute vs Relative path

Les paths relatifs sont donnés en fonction du répertoire courant (current working directory). 
Les paths absolues sont donnés en fonction du répertoire racine (root) du système de fichiers.

## Travailler avec des fichiers et des dossiers

#### Questions
> - Comment créer, copier et supprimer des fichiers et dossiers?
> - Comment éditer des fichiers?

#### Objectifs
> - Créer des fichiers qui correspondent à un diagramme.
> - Créer des fichiers de cette hiérachie en utilisant un éditeur.
> - Supprimer, copier et déplacer des fichiers et dossiers.

## Recommandation pour les noms de fichiers et de dossiers

Des noms complexes rendent les commandes plus difficiles.

1. N'utiliser pas d'espaces
2. Ne commencez pas les noms avec un **'-'**
3. Éviter les symboles! Ils ont une autre référence en ligne de commande

## Commandes de modifications

#### Créer un dossier

```bash
    $ mkdir thesis
```

#### Créer un fichier avec un éditeur

```bash
    $ nano test_draft.txt
```

Suivre les commandes pour l'édition (fn F2 sur mac pour quitter ou ctrl-X sur autre) 

#### Créer un fichier vide

```bash
    $ touch mon_fichier.txt
```

#### Supprimer des fichiers

```bash
    $ rm mon_fichier.txt
```

#### Supprimer un dossier

```bash
    $ rmdir mon_dossier
```

Un dossier avec des contenus:
```bash
    $ rm -r mon_dossier
```

Pour supprimer un dossier avec son contenu, on utilise la commande **'rm'** et non **'rmdir'**

*En ligne de commande, il n'y a pas de retour en arrière (Pas de corbeille)! Faites attention lorsque vous supprimé.*

Plus sécuritaire:
```bash
    $ rmdir -i mon_dossier
```

#### Déplacer des fichiers

```bash
    $ mv test.txt thesis/test.txt
```

*Faire attention à l'écrasement de fichier lorsque vous déplacez des fichiers. 
S'il y a un fichier du même nom dans le répertoire de réception, il sera écrasé.*

#### Renommer un fichier

```bash
    $ mv test.txt text.txt
```

#### Copier des fichiers et des dossiers

```bash
    $ cp thesis/test.txt test.txt
```

#### Faire un back-up

```bash
    $ cp -r thesis thesis-backup
```

#### 'Wildcards'

**'\*'** remplace une chaîne de caractère.

**'?'** remplace un seul caractère.

#### Trouver tous les fichiers ayant une certaine extension:

```bash
    $ ls *.txt
```

#### Trouver tous les fichiers ayant un charactère qui varie peu importe l'extension:

```bash
    $ ls ?_sherbrooke.*
```

#### Exercice

## TODO: Définir

## Filtres et pipes

#### Questions: 
> - Comment combiner plusieurs commandes?

#### Objectifs
> - Rediriger la sortie d'une commande à un fichier
> - Traiter un fichier 
> - Construire un pipeline de traitement de plusieurs étapes
> - Comprendre la philosopie Unix 'small pieces, loosely joined'

## Exemples de combinaison

#### Aller à un dossier et lister les contenus

```bash
    $ cd data-shell; ls -F
```

#### Aller à un dossier et lister le nombre de mots des fichiers

```bash
    $ cd data-shell; wc *.pdb
```

Ou seulement le nombre de lignes:
```bash
    $ cd data-shell; wc -l *.pdb
```

#### Rediriger le contenu vers un fichier

```bash
    $ wc *.pdb > lengths.txt
```

*Commun en Python (dans un venv):*

```bash
    $ pip freeze > requirements.txt
```

#### Imprimer le contenu d'un fichier 

```bash
    $ cat requirements.txt
```

*Faire attention avec des fichiers très large.*

```bash
    $ less requirements.txt
```

#### Classer le contenu d'un fichier

```bash
    $ sort -n lenghts.txt
```

***'n'** utiliser pour spécifier que le champ est numérique*

Le fichier n'est pas modifier. Le contenu imprimé est simplement classé.

Pour enregistrer le contenu dans un nouveau fichier:

```bash
    $ sort -n lenghts.txt > sorted_lengths.txt
```

#### imprimer du texte:

```bash
    $ echo The echo command prints things
```

Enregistrer dans un fichier:

```bash
    $ echo The echo command prints things > echo_text.txt
```

*Le symbole '>' écrase le fichier*

#### Ajouter du contenu à un fichier avec '>>':

```bash
    $ echo The echo command prints things >> echo_text.txt
```

##### Imprimer le début ou la fin d'un fichier

```bash
    $ head -n 3 lengths.txt > l_up.txt
    $ tail -n 2 lengths.txt >> l_up.txt
```

### Les pipes:

Les pipes prennent la sortie de la première commande et l'envoie commen entré à la deuxième. 
L'ordinateur créera des fichiers temporaires en mémoire ou exécutera n'importe qu'elle tâche qu'il a besoin.

```bash
    $ wc -l *.pdb | sort -n
```

Chercher le total du nombre de mot dans tous les fichiers: 

```bash
    $ wc -l *.pdb | sort -n | tail -n 1
```

## Le principe du Shell

## TODO: place graphiqe

Au lieu de créer des programmes immenses qui exécutent plusieurs tâches, les programmeurs Unix se concentre sur le développement
de petits outils qui font une tâche parfaitement et qui peuvent fonctionner ensemble. Le modèle de développement s'appel: 'pipes and filters.'
C'est une des grandes raisons de pourquoi le Shell Unix est si populaire.

Les filtres sont des programmes comme 'wc' ou 'sort', ils appliquent une fonction à des intrants et envoie une sortie.
Presque tous les outils Unix fonctionnent de cette façon: 
- Lire des intrants (standard input ou stdin), 
- Appliquer une fonction aux intrants
- Écrire une sortie (standard out ou stdout)

## Rediriger des intrants

Comme utiliser **'>'** pour rediriger les sorties vers un fichier, il est possible de lire les contenus d'un fichier avec **'<'**.

Example: 

```bash
    $ wc -l notes.txt
```

Le nom du fichier et ces contenus sont passés à la fonction.

```bash
    $ wc -l < notes.txt
```

Les contenus du fichiers sont seulement passés à la fonction

## Les boucles

#### Questions
> - Comment performer les mêmes actions sur différents niveaux de fichiers?

#### Objectifs
> - Écrire une boucle qui s'applique sur plusieurs fichiers distincts
> - Suivre les valeurs d'une variable durant l'exécution d'une boucle
> - Expliquer la différence entre le nom d'une variable et sa valeur
> - Expliquer pourquoi certains espaces et autres ponctuations ne devraient pas être utilisés
> - Démontrer comment obtenir les commandes récemment exécuter
> - Exécuter les commandes récemment utiliser sans les réécrire.

## Commandes/Exemples de boucles

Aller dans le répertoire creatures.

Le symbole **'$'** est utilisé pour désigner une variable. 

#### Retourner les trois premières lignes de plusieurs fichiers:
```bash
$ for filename in basilisk.dat unicorn.dat
> do
>    head -n 3 $filename
> done
```
L'indentation n'est pas obligatoire comme en Python, mais aide à la lisibilité.


#### Lister les contenus d'un dossier et les sous dossiers

Aller au répertoire 'molecules'.
```bash
for filename in c*
> do
>   ls $filename
> done
```

#### Ajouter les contenus de fichiers à un seul fichier:
```bash
for datafile in *.pdb
> do
>   cat $datafile >> all.pdb
> done
```

#### Pourquoi éviter les espaces:

Si un fichier contient des espaces, il est nécessaire de l'encapsuler comme suit:

```bash
$ for filename in "red dragon.dat" "purple unicorn.dat"
> do
>     head -n 100 "$filename" | tail -n 20
> done
```


#### Copier un fichier dans plusieurs dossiers:

```bash
$ for filename in *.dat
> do
>     cp $filename original-$filename
> done
```


#### Afficher l'historique de commande

```bash
history | tail -n 5
```

#### Nested Loop
```bash
$ for species in cubane ethane methane
> do
>     for temperature in 25 30 37 40
>     do
>         mkdir $species-$temperature
>     done
> done
```

## Les scripts Shell 

#### Questions
> - Comment sauvegarder et réutiliser des commandes?

#### Objectifs
> - Écrire un script qui exécute une série de commande sur plusieurs fichiers distincts
> - Exécuter un script à partir de la ligne de commande
> - Écrire un script qui reçoit des intrants d'un usager à partir de la ligne de commande
> - Créer des pipelines de traitement qui inclus plusieurs scripts

Les scripts sont ce qui rend le shell si puissant. 
L'habileté de sauvegarder une série de commande dans un scripts et l'exécuter avec un seule commande.

## Commande pour créer des scripts shell

```bash
    $ cd molecules
    $ nano middle.sh
```

Ou: 
```bash
    $ cd molecules
    $ touch middle.sh
    $ open -a "textEdit" middle.sh 
    $ open -a "pyCharm" middle.sh
```

Les mêmes commandes peuvent être passer à notre script:
```bash
head -n 15 octane.pdb | tail -n 5
```

Le script peut maintenant être appelé du shell:

```bash
    $ bash middle.sh
```

#### Modifier le script pour passer un nom de fichier à celui-ci

On remplace le nom de fichier par '$1' pour désigné le premier argument passé à la ligne de commande.

```bash
head -n 15 "$1" | tail -n 5
```
*Mettre la variable entre double guillemets assure qu'un argument passé avec un espace sera lu par notre commande.*

La fonction peut maintenant être appelé sur n'importe quelle fichier:
```bash
    $ bash middle.sh octane.pdb
```

#### Modifier le script pour prendre un nombre de lignes différents:
```bash
head -n "$2" "$1" | tail -n "$3"
```

Il est maintenant possible d'obtenir les lignes désirées dans le milieu d'un fichier::
```bash
    $ bash middle.sh octane.pdb 15 10
```

#### Commenter son code

Comme en python, il est possible de commenter son code en utilisant des **'#'**:

# Select lines from the middle of a file.
# Usage: bash middle.sh filename end_line num_lines
```bash
# Sélectionner des lignes dans le milieu d'un fichier.
# Usage: bash middle.sh filename end_line num_lines
head -n "$2" "$1" | tail -n "$3"
```

#### Passer un nombre non-défini d'arguments

Le symbole **'$@'** est utilisé pour passer un nombre indéfini d'arguments à la ligne de commande.

```bash
# Script to find unique species in csv files where species is the second data field
# This script accepts any number of file names as command line arguments

# Loop over all files
for file in $@ 
do
	echo "Unique species in $file:"
	# Extract species names
	cut -d , -f 2 $file | sort | uniq
done
```

#### Note sur l'historique de commande

Une commande est toujours enregistrer dans l'historique des commandes avant d'être exécuter. 
Ceci permet de comprendre plus facilement des erreurs lors de l'exécution.

#### Questions
> - Comment sauvegarder et réutiliser des commandes?

#### Objectifs
> - Écrire un script qui exécute une série de commande sur plusieurs fichiers distincts
> - Exécuter un script à partir de la ligne de commande
> - Écrire un script qui reçoit des intrants d'un usager à partir de la ligne de commande
> - Créer des pipelines de traitement qui inclus plusieurs scripts


## Trouver des éléments

#### Questions
> - Comment trouver des fichiers?
> - Comment trouver des éléments dans des fichiers?

#### Objectifs
> - Utiliser **'grep'** pour sélectionner des lignes de fichiers
> - Utiliser **'find'** pour trouver des fichiers 
> - Utiliser la sortie d'une commande comme entré à une subséquente

## Exemple trouver les lignes d'un document texte

#### Montrer les contenus du fichiers 'haiku.txt'
```bash
    $ cd Desktop/data-shell/writing
    $ cat haiku.txt
```

#### Trouver les lignes du fichier contenant une chaîne de charactères spécifique (pas juste un mot):
```bash
    $ grep The haiku.txt
```

*Note sur la chaîne de charactères: exécuter cette commande avec 'The' retournerait aussi des lignes avec des mots comme Thesis.*

#### Pour limiter à un mot, on peut passer un flag:
```bash
    $ grep -w The  haiku.txt
```

#### On peut passer une phrase avec la chaîne de charactères entre guillemets:
```bash
    $ grep -w "is not"  haiku.txt
```

#### D'autres flags intéressant:

- **'-n'** retourne le numéro de ligne
- **'-i'** ignore si les charactères sont en majuscule ou minuscule
- **'-v'** inverse la recherche (sélectionne ceux ne contenant pas la chaîne de charactères)

## Utiliser des expressions régulières

Les expressions régulières permettent de faire des recherches plus spécifique de séries de charactères. 
Comme les wildcards **'\*'** et **'?'** utiliser au début pour lister des fichiers répondant à des conditions plus spécifiques.

Par exemple trouver tous les lignes contenant des mots ayant la lettre 'o' en deuxième position:
```bash
    $ grep -E '^.o'  haiku.txt
```

## Trouver des fichiers

#### Trouver l'ensemble des fichiers du répertoire courant
```bash
    $ find .
```

#### Trouver l'ensemble des dossiers d'un répertoire

```bash
    $ find . -type d
```

#### Trouver l'ensemble des fichiers d'un répertoire

```bash
    $ find . -type f
```

#### Trouver les fichiers par leur nom

Ne pas faire:
```bash
    $ find . -name *.txt
```

*Le wildcard exécutera en premier et un seul résultat sera retourner.*

Pour obtenir l'ensemble des fichiers correspondant:
```bash
    $ find . -name '*.txt'
```
*Le wildcard exécutera après la commande et non avant.*

#### Compter les lignes avec des fichiers trouver:
```bash
    $ wc -l $(find . -name '*.txt')
```

#### Utiliser 'grep' et 'find' ensemble:
```bash
    $ grep "FE" $(find . -name '*.txt')
```

## Conclusion

La ligne de commande est un outil puissant qui permet d'automatiser des tâches complexes.

Maîtriser le Shell permet de développer des solutions innovateurs en utilisant des programmes déjà existants. 

Maintenant que les principes du Shell sont maîtrisés, vous pouvez aller voir (*contenu à venir si pas encore disponible*):
- [Transformer des scripts Python pour la ligne de commande](../python-script-cl/python-script-cl-en.MD)
- [Utiliser la ligne de commande dans des scripts Python](../calling-cl-python/calling-cl-python-en.MD)
- [Efficiently scaling remote sensing image corrections with the CL and Python](../calling-cl-python/calling-cl-python-en.MD)


Contenu initalement publié sur [mon site](zacharydeziel.com).

## Source du contenu:

Gabriel Devenyi, Christina Koch, and Ashwin Srinath (eds): "Software
Carpentry: The Unix Shell."  Version 2016.06, June 2016,
https://github.com/swcarpentry/shell-novice, 10.5281/zenodo.57544.



