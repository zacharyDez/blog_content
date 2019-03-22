# Introduction à *Black* - formateur automatique Python

*Black* est un formateur automatique pour Python. L'outil permet d'uniformiser le travail d'équipe de développement.
Le projet vise à minimiser le temps passé par les développeurs sur le format de leur travail pour qu'il se concentre sur leur contenu.

**Documentation**:
- [Standards Python](https://www.python.org/dev/peps/)
- [Documentation *Black*](https://black.readthedocs.io/en/stable/)

## Installation

```bash
    $ pip install black
```

## Utilisation simple

Une première utilisation de l'outil est de simplement de l'appliquer à la racine du projet:

```bash
    $ black dossier_racine
```

Voilà, votre code est formaté! C'est simple, rapide et suffisant pour des projets personnels de petite taille. 

## Utilisation avancée

Un *hook* est un programme qui déclenche des actions sur des commandes git. 
Il est possible de définir des actions à exécuter à tout moment de notre processus de contrôle de version: [documentation sur les *hooks*](https://git-scm.com/docs/githooks).

Il est possible de définir un *hook* pour qu'à chaque fois que la commande git commit est exécuté,
notre code se fait formater par *Black*.

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

Au prochain commit, l'environnement git sera initialisé et notre *hook Black* sera exécuté. 
Le formatage sera réalisé automatiquement à chaque *commit*.

#### Note

Il est possible d'aller modifier le *.toml* file de *Black* pour modifier certaines configurations du formatage automatique (
ex: nombre de caractères par lignes).

*Contenu initialement publié sur [mon site](zacharydeziel.com).*

