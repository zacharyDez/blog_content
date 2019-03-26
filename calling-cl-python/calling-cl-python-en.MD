# Utiliser la ligne de commande avec des scripts Python
## Introduction au module *subprocess* de Python

## Préparation

Si vous avez besoin d'un rappel sur la ligne de commande: [Introduction au Shell et à la ligne de commande](http://zacharydeziel.com/post/3).

L'objectif de l'article est de continuer l'introduction à la ligne de commande et d'agir comme préparation aux deux prochains sujets:

- [Adapting Python Scripts for the command line](http://zacharydeziel.com/post/5).
- [Calling Python scripts to automate corrections to remote sensing images]().
 *En progrès, voir sur [Git](https://github.com/zacharyDez/gdal_dir_calc).*


## Contexte

Avant Python 3.5, il y avait plusieurs modules pour interagir avec le Shell (os.system, os.spawn).

Le module *subprocess* combine les fonctionnalités de ces modules. 

Il permet d'exécuter des commandes du Shell et d'interagir avec les intrants/sortants/erreurs des commandes.

Documentation sur le [module *subprocess*](https://docs.python.org/3/library/subprocess.html).

Documentation sur la proposition du module *subprocess*: [PEP 324](https://www.python.org/dev/peps/pep-0324/).

## Pourquoi appeler des commandes Shell avec Python?

Les commandes du Shell permettent d'interagir avec plusieurs programmes et de les combiner de façon spécifique à un contexte.

Par contre, les scripts Shell sont parfois d'une grande complexité et difficile à maintenir.

Des scripts Python (quand ils sont bien réussis) ont la qualité d'être faciles à lire et comprendre.

Appeler les commandes du Shell dans des scripts Python permet d'avoir accès à toutes les fonctionnalités du Shell
tout en ayant les fonctionnalités de haut-niveau de Python.

## Utilisation du module *subprocess*

La première méthode recommandée pour utiliser *subprocess* est la fonction *run()*. 

Le principe de l'utilisation de la commande *run* est de mettre chaque argument de la commande dans une liste:

```python
from subprocess import run

run(args=['ls', '-F', '..'])
```

Ce script imprime une liste des dossiers et des fichiers du répertoire parent.

Similairement, on peut obtenir l'ensemble des sous-dossiers et fichiers:
```python
from subprocess import run

run(['ls', '-F', '-R' '..'])
```

Un argument intéressant est *capture_output* qui permet de stocker la sortie des commandes exécutées. 
Par défaut, sa valeur est *False*. 

```python
from subprocess import run

cmd = run(args=['ls', '-F', '-R', '..'], capture_output=True)
```

Dépendamment de la commande, manipuler les sorties enregistrées dans les variables peut être plus complexe.

Un exemple de traitement pour obtenir une liste Python de l'ensemble des fichiers:
 
```python
# caster la variable cmd en str
# double '\' nécessaire pour split '\n'
out = str(cmd.stdout).split('\\n')
```

Il peut être redondant d'entrer l'ensemble des arguments dans une liste. 
Le module *shlex* est utile pour transformer une commande entière en arguments pour la fonction run.

```python
from subprocess import run
import shlex

cmd = 'ls -F -R ..'

run(args=shlex.split(cmd))
```

Il serait possible de saisir une commande de l'usager par la ligne de commande.

Similairement, la fonction *Popen* peut-être appelée pour exécuter des commandes
```python
from subprocess import Popen
import shlex

cmd = 'ls -F -R ..'

Popen(args=shlex.split(cmd))
```

La fonction Popen permet de lancer des commandes plus complexes, notamment d'utiliser des pipes plus facilement.

Vous pouvez voir les différentes options à l'aide de la [documentation](https://docs.python.org/3/library/subprocess.html).

## Conclusion

La ligne de commande permet d'assembler des traitements simples en pipelines de traitement complexes.

Les prochains sujets sont basés sur l'introduction au Shell et 
à l'habileté d'exécuter les commandes Shell à l'intérieur de scripts Python.

- [Adapter des scripts Python à la ligne de commande](http://zacharydeziel.com/post/5)

- [Apprendre comment corriger des images de télédétection avec des scripts déjà existants et adapter à la ligne de commande]()

*En progrès, voir sur [Git](https://github.com/zacharyDez/gdal_dir_calc).*


