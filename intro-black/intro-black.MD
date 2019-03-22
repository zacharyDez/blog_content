# Introduction à *Black* - formatteur automatique Python

*Black* est un auto-formatteur pour Python. L'outil permet d'uniformiser le travail d'équipe de développement.
Le projet vise à minimiser le temps passer par les développeurs sur le format de leur travail pour qu'il se concentre sur leur contenu.

**Documentation**:
- [Standards Python](https://www.python.org/dev/peps/)
- [Documentation *Black*](https://black.readthedocs.io/en/stable/)

## Installation

```bash
    $ pip install black
```

## Utilisation Simple

Une première utilisation de l'outil est de simplement de l'appliquer à la racine du projet:

```bash
    $ black dossier_racine
```

Voilà, votre code est formatter! C'est simple, rapide et suffisant pour des projets personnels de petite taille. 

## Utilisation Avancé

Un *hook* est un programme qui déclenche des actions sur des commandes git. 
Il est possible de définir des actions à exécuter à tout moment de notre processus de contrôle de version: [documentation sur les *hooks*](https://git-scm.com/docs/githooks).

Il est possible de définir un *hook* pour qu'à chaque fois que la commande git commit est exécuter,
notre code se fait formatter par *Black*.

#### Étapes pour configurer *Black* en pre-commit: 

-  Installer l'outil pre-commit:
```bash
    $ pip install pre-commit
```
-  Ajouter pre-commit à votre fichier *requirements.txt*:
```bash
    $ pip freeze > requirements.txt
```
- Définir les *hooks* désirés dans le fichier de configuration pre-commit (nommer *.pre-commit-config.yaml):
```bash
repos:
-   repo: https://github.com/ambv/black
    rev: stable
    hooks:
    - id: black
      language_version: python3.7
```
- Exécuter la commande pour installer les hooks dans notre répertoire *.git/*:
```bash
    $ pre-commit install
```


## Conclusion

La ligne de commande est un outil puissant qui permet d'automatiser des tâches complexes.

Maîtriser le Shell permet de développer des solutions innovateurs en utilisant des programmes déjà existants. 

Maintenant que les principes du Shell sont maîtrisés, vous pouvez aller voir (*contenu à venir si pas encore disponible*):
- [Transformer des scripts Python pour la ligne de commande](../python-script-cl/python-script-cl-en.MD)
- [Utiliser la ligne de commande dans des scripts Python](../calling-cl-python/calling-cl-python-en.MD)
- [Efficiently scaling remote sensing image corrections with the CL and Python](../calling-cl-python/calling-cl-python-en.MD)


Contenu initialement publié sur [mon site](zacharydeziel.com).

## Source du contenu:

Gabriel Devenyi, Christina Koch, and Ashwin Srinath (eds): "Software
Carpentry: The Unix Shell."  Version 2016.06, June 2016,
https://github.com/swcarpentry/shell-novice, 10.5281/zenodo.57544.