# Secret Santa

Ce repo contient la description et le développement du cas technique "secret santa" proposé par OuiHelp.

## Description

On est proche de Noël, nous sommes un groupe d'amis, dont certains sont en couple, et nous voulons organiser un "secret santa" (un échange de cadeaux entre les membres du groupe). Pour ce "secret santa" comme nous sommes un groupe exigeant notre répartition des cadeaux (le "qui donne à qui") doit répondre à 3 règles :

1. Chaque membre du groupe doit faire un et un seul cadeau, chaque membre du groupe doit recevoir un et un seul cadeau.
2. Il ne peut pas y avoir de réciprocité dans la répartition : si A offre à B, alors B ne peut pas offrir à A.
3. Il ne peut pas y avoir de cadeaux entre membres d'un couple : si A et B sont en couples, alors A n'offre pas à B et B n'offre pas à A.

Un jeux de données de test pour les membres et pour les couples :

    PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"]
    COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]

Le but de l'exercice est d'écrire un "logiciel", qui calcule et retourne une répartition possible des cadeaux.

## Reformulation

Pour mieux visualiser le problème et les possibles cadeaux des uns envers les autres, il est possible de modéliser le problème sous forme de graphe:

- chaque sommet représente un membre du groupe
- chaque arête représente un possibilité de cadeau d'un membre à un autre

Par exemple, en utilisant le jeux de données d'example (chaque membre est désigné par l'intial de son prénom):

![image](graph-example.png)

Avec cette représentation, le problème peut être reformuler comme suit:
> Trouver le chemin reliant chaque sommet exactement une fois et revenant au sommet de départ.

## Comment lancer secret-santa

```bash
python secret-santa.py
```


## Améliorations