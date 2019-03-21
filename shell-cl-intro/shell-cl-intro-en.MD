# Introduction au shell et à la ligne de commande

Contenu initalement publié sur [mon site](zacharydeziel.com)


## Introduction au Shell

##### Question

- C'est quoi la ligne de commande et pourquoi je devrais l'utiliser?

##### Objectifs:
- Comprendre les liens entre les usagers et l'ordinateur
- Comprendre pourquoi et quand les lignes de commandes sont plus adaptées que des interfaces graphiques

#### Contexte

À un haut-niveau les ordinateurs peuvent:
- Exécuter un program
- Stocker des des données
- Communiquer entre eux
- Intéragir avec des usagers

Ils peuvent faire ses tâches de plusieurs méthodes différentes par l'entremise du clavier, d'une souris, d'un écran tactile ou même par reconnaissance de la voix.

Nous sommes tous familiers avec des interfaces graphiques (GUI) qui consiste en des fenêtres, des icons et des pointeurs. 
Ils sont faciles à apprendre and excellent pour exécuter des tâches simples. Particulièrement, lorsque qu'un simple 'clique' 
peut se traduire en 'effectue cette tâche de haut niveau d'abstraction'. 
Cette magie dépend de plusieurs petites tâches simples and d'avoir accès à des programmes qui font ces tâches simples.
 
Si vous désirez accomplir des tâches plus complexes et appliquer à un domaine spécifique, avoir des connaissances du shell sont nécessaires pour communiquer avec l'ordinateur.
La connaissance de simple commandes permettent d'automatiser une grande charge de travail.

Le coeur d'une interface de ligne de commande est la relation lecture-évaluation-sortie (*read-evaluate-print, REPL* ). 
Quand une commande est saisie, elle est évaluer et ensuite une sortie (résultat) est imprimée.

## Définition du Shell

Le Shell est un programme qui utilise d'autres programmes pour exécuter les calculs au lieu de l'effectuer lui même. 
Il y a plusieurs Shell qui existe. Bash est le shell par défaut des systèmes d'opérations Unix and de plusieurs extensions du Shell sur Windows.

#TODO: Insérer image du Shell: example ls avec sortie

## Comment que le Shell comprend les commandes and ces arguments?

Chaque commande à un programme qui est stocké sur l'ordinateur et le shell possède une liste des endroits où chercher 
pour les commandes (dans la fameuse variable PATH).

#### Logic du Shell:
1. Lire la commande saisie (séparation par espace et ';' entre les commandes)
2. Évaluer la commande:
    - Trouver le programme de la commande
    - Exécuter la commande en y passant les arguments
3. Imprimer la sortie de la commande.

Si la commande n'est pas trouvée, des messages d'erreurs seront imprimées comme sortie.

#### Différence avec un GUI

Un GUI vous présente des options et vous êtes limités par ces options.
Avec une ligne de commande, il est possible d'établir des combinaisons plus personnalisées.

#### Flexibilité et automatisation

Le shell permet de prendre des commandes existantes et de développer des pipelines de traitement plus avancés.
Cette capacité est fondamentale pour traiter des grands volumes de données. 
Il est possible d'écrire des séquences de commandes dans des scripts pour avoir des méthodes reproductibles.


## Naviguer des dossiers et des fichiers

#### Questions
- Comment se déplacer sur notre ordinateur?
- Comment connaître les fichiers sur mon ordinateur?
- Comment spécifier l'emplacement d'un dossier ou d'un fichier sur mon ordinateur?

#### Objectifs
- Expliquer les similarités et les différences entre un dossier et un fichier.
- Traduire un path absolue en path relatif et vice-versa
- Construire des paths qui identify des fichiers ou dossiers spécifique.

La partie du système d'opération (OS) qui s'occupe de la gestion de fichier se nomme le système de fichier. 
Il organise nos données en fichiers ou en dossier. 
Les fichiers ont de l'information, tandis que les dossiers sont composés de fichiers ou de d'autres dossiers.

Plusieurs commandes existent pour créer, inspecter, renommer et supprimer des fichiers ou dossiers.

## Commandes de navigation du système de fichiers

#### Notes différences de systèmes d'opérations

Les machines windows séparent les dossiers par '\' et les machines Unix par '/'.

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

Le flag -F permet de savoir quel type de contenu est lister (avec les '/')

```bash
    python-exception-handling-intro/ shell-cl-intro/
```

#### Obtenir de l'aide pour une commande

Obtenir le manuel de la commande: chercher unix man page.

```bash
    $ man ls
```

Les manuels sont disponibles en ligne
# TODO: check if works on windows
Obtenir de l'aide 
```bash
    $ ls --help
```

#### Outils intéressant de ls

Présenter tous les dossiers et fichiers de façon récursive:
```bash
    $ ls -R
```

Présenter les dossiers et fichiers par date de modificaiton:
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

Le ~ est interpréter comme référence au dossier mère de l'usager (home directory).

```bash
    $ cd ~/Desktop
```

Constructs absolute path

#### Absolute vs Relative path

Les paths relatifs sont donnés en fonction du répertoire courant (current working directory). 
Les paths absolues sont donnés en fonction du répertoire racine (root) du système de fichiers.

## Travailler avec des fichiers et des dossiers

#### Questions
- Comment créer, copier et supprimer des fichiers et dossiers?
- Comment éditer des fichiers?

#### Objectifs
- Créer des fichiers qui correspondent à un diagramme.
- Créer des fichiers de cette hiérachie en utilisant un éditeur.
- Supprimer, copier et déplacer des fichiers et dossiers.

## Conclusion

La ligne de commande est un outil puissant qui permet d'automatiser des tâches complexes.

Maîtriser le Shell permet de développer des solutions innovateurs en utilisant des programmes déjà existants. 

Contenu initalement publié sur [mon site](zacharydeziel.com)

Source du contenu: [Software carpentry](https://swcarpentry.github.io/shell-novice/)



