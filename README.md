# Simulateur d’ordonnanceur de processus (Python)

Ce projet est une **simulation d’un ordonnanceur de processus** simple en Python, inspirée du fonctionnement d’un processeur avec gestion des **priorités multiples**.


## Fonctionnement

Le programme gère une liste de **files de priorités**, où :
- Chaque sous-liste contient des processus d’une même priorité.
- Plus la priorité est faible numériquement (ex: `0`), plus elle est **importante**.


### Principe
À chaque cycle d’horloge :
1. Si aucun processus n’est en cours et qu’il reste des processus en attente :
   - Le processus de la plus haute priorité est élu pour s’exécuter.
2. Si un processus est en cours :
   - S’il a terminé son temps CPU : il est retiré.
   - Sinon : il consomme un cycle CPU, puis :
     - Si un autre processus plus prioritaire est en attente : préemption.
     - Sinon : le processus continue, mais sa priorité baisse légèrement.


## Structure du code

- **`class Processus`** : représente un processus (PID, priorité, temps CPU total, temps utilisé)
- **`meilleure_priorite()`** : renvoie la priorité de la première file non vide
- **`prioritaire()`** : renvoie et retire le premier processus de la première file non vide
- **`gerer()`** : boucle principale simulant le comportement du processeur


## Exemple d’exécution

===== Cycle 1 =====
Nouveau processus en cours : P1 (priorité 0)

===== Cycle 2 =====
Exécution : P1 (prio 0) [1/10]
Préemption : un processus de priorité 0 est en attente.
Nouveau processus élu : P2 (priorité 0)

...

===== Cycle 28 =====
P1 terminé après 10 cycles CPU.

Simulation terminée en 28 cycles totaux.


## Améliorations possibles

- Ajouter un affichage graphique de l’état des files de priorités
- Gérer plusieurs cœurs de processeur
- Introduire un quantum de temps (ordonnancement par tourniquet)
- Exporter les logs dans un fichier `.txt` ou `.csv`


## Auteur

Projet développé par Mahé Da Silva, élève en terminale spécialité NSI.  
Objectif : modéliser un ordonnanceur de processus simple pour mieux comprendre la gestion CPU et les files de priorités.
