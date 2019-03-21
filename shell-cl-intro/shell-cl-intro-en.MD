# Introduction au Shell et à la ligne de commande

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

Le Shell est un program qui utilise d'autres programmes pour exécuter les calculs au lieu de l'effectuer lui même. 
Il y a plusieurs Shell qui existe. Bash est le shell par défaut des systèmes d'opérations Unix and de plusieurs extensions du Shell sur Windows.

#TODO: Insérer image du Shell: example ls avec sortie

## Comment que le Shell comprend les commandes and ces arguments?

Chaque commande à un programme qui est stocké sur l'ordinateur et le shell possède une liste des endroits où chercher 
pour les commandes (Dans la fameuse variable PATH).

#####Logic du Shell:
1. Lire la commande saisie (séparation par espace et ';' entre les commandes)
2. Évaluer la commande:
    - Trouver le programme de la commande
    - Exécuter la commande en y passant les arguments
3. Imprimer la sortie de la commande.

Si la commande n'est pas trouvé, des messages d'erreurs seront imprimés comme sortie.

## Différence avec un GUI

Un GUI vous présente des options et vous êtes limités par ces options.
Avec une ligne de commande, il est possible d'établir des combinaisons plus personnalisées.

## Flexibilité et automatisation

Le shell permet de prendre des commandes existantes et de développer des pipelines de traitement plus avancé.
Cette capacité est fondamentale pour traiter des grands volumes de données. 
Il est possible d'écrire des séquences de commandes dans des scripts pour avoir des méthodes reproductibles.


## Conclusion

La ligne de commande est un outil puissant qui permet d'automatiser des tâches complexes.

Maîtriser le Shell permet de développer des solutions innovateurs en utilisant des programmes déjà existants. 

Contenu initalement publié sur [mon site](zacharydeziel.com)

Source du contenu: [Software carpentry](https://swcarpentry.github.io/shell-novice/)



