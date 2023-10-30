# Secret Santa

Ce repo contient la description et le développement du cas technique "secret santa" proposé par OuiHelp.

## Description

On est proche de Noël, nous sommes un groupe d'amis, dont certains sont en couple, et nous voulons organiser un "secret santa" (un échange de cadeaux entre les membres du groupe). Pour ce "secret santa" comme nous sommes un groupe exigeant notre répartition des cadeaux (le "qui donne à qui") doit répondre à 3 règles :

1. Chaque membre du groupe doit faire un et un seul cadeau, chaque membre du groupe doit recevoir un et un seul cadeau.
2. Il ne peut pas y avoir de réciprocité dans la répartition : si A offre à B, alors B ne peut pas offrir à A.
3. Il ne peut pas y avoir de cadeaux entre membres d'un couple : si A et B sont en couples, alors A n'offre pas à B et B n'offre pas à A.

Un jeux de données d'example, de test pour les membres et pour les couples :

    PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"]
    COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]

Le but de l'exercice est d'écrire un "logiciel", qui calcule et retourne une répartition possible des cadeaux.

## Première solution: brute force search

Sélectionner au hasard un premier membre du groupe pour générer les différentes suites de membres possibles. Une suite de membres est valide si chaque membre du groupe apparaît une seule fois et si deux membres en couple ne sont pas consécutifs. Le premier et le dernier membre de la suite ne doivent pas être en couple non plus.

Par example, la représentation de la suite de membre par la liste python ["Florent", "Jessica", "Coline", "Ambroise", "Emilien", "Bastien"] indique que Florent offre un cadeau à Jessica, qui offre un cadeau à Coline, et ainsi de suite jusqu'à Bastien qui offre un cadeau à Florent. Cette solution n'est pas valide puisque Florent et Jessica sont en couple.

Une solution valide est ["Florent", "Coline", "Jesssica", "Ambroise", "Emilien", "Bastien"].

Complexité:
- temporelle: `O(!n)`
- mémoire: `O(n)` 

## Reformulation

Pour mieux visualiser le problème et les possibles cadeaux des uns envers les autres, il est possible de modéliser le problème sous forme de graphe:

- chaque sommet représente un membre du groupe
- chaque arête représente un possibilité de cadeau d'un membre à un autre

Par exemple, en utilisant le jeux de données d'example (chaque membre est désigné par l'intial de son prénom):

![image](graph-example.png)

Avec cette représentation, le problème peut être reformuler comme suit:
> Trouver le chemin reliant chaque sommet exactement une fois et revenant au sommet de départ.

## Comment lancer *secret-santa*

Nécessaire au lancement du programme: `python >= 3.4` 

Pour lancer *secret-santa*:

```bash
python secret-santa.py data-test.json
```

Accéder aux différentes options:

```bash
python secret-santa.py --help
```

## Sources de données supportées

- Fichier au format `json` contenant un dictionnaire avec pour clés :
    - `"PEOPLE"` (`List[str]`): liste des membres du groupes
    - `"COUPLES"` (`List[List[str]]`): liste des couples 

## Développement

Créer un environnement virtuel python:

```bash
python -m venv env
```

Activé l'environnement:

```bash
source env/scripts/activate
```

Installer les dépendances de dévéloppement et de test:

```bash
pip install -r requirements-dev.txt
```

Lancer la suite de tests:

```bash
pytest
```

## Améliorations