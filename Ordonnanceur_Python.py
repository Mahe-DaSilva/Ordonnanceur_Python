# ==============================
#  Simulation d’un ordonnanceur de processus
# ==============================

class Processus:
    """
    Classe représentant un processus simulé.
    Attributs :
    - PID : identifiant unique du processus
    - priorite : niveau de priorité (0 = plus prioritaire)
    - temps_utilisation : temps CPU déjà utilisé
    - temps_CPU : temps CPU total nécessaire
    """
    def __init__(self, PID, priorite, temps_CPU):
        self.priorite = priorite
        self.PID = PID
        self.temps_utilisation = 0
        self.temps_CPU = temps_CPU

    def __repr__(self):
        """Affichage lisible du processus"""
        return f"P{self.PID}(prio={self.priorite}, util={self.temps_utilisation}/{self.temps_CPU})"


# --- Création des processus ---
P1 = Processus(PID=1, priorite=0, temps_CPU=10)
P2 = Processus(PID=2, priorite=0, temps_CPU=7)
P3 = Processus(PID=3, priorite=0, temps_CPU=5)

# --- Initialisation des files de priorités ---
# Chaque sous-liste correspond à une file de priorité
liste_files = [[], [], []]
liste_files[P1.priorite].append(P1)
liste_files[P2.priorite].append(P2)
liste_files[P3.priorite].append(P3)


# ==============================
#  Fonctions de gestion
# ==============================

def meilleure_priorite(liste_files):
    """
    Renvoie l'indice (priorité) de la première file non vide.
    Retourne None si toutes les files sont vides.
    """
    if not liste_files:
        return None

    for i, sous_liste in enumerate(liste_files):
        if sous_liste:
            return i
    return None


def prioritaire(liste_files):
    """
    Renvoie et retire le premier processus de la première file non vide.
    Retourne None si toutes les files sont vides.
    """
    if not liste_files:
        return None

    for sous_liste in liste_files:
        if sous_liste:
            return sous_liste.pop(0)
    return None


def gerer(p, liste_files):
    """
    Simule la gestion d’un processeur avec des files de priorité.
    À chaque cycle :
      - Si aucun processus n’est en cours : en sélectionner un
      - Si un processus est en cours :
          * S’il a fini : le retirer
          * Sinon : incrémenter son temps d’utilisation
          et gérer la priorité (préemption éventuelle)
    """
    cycle = 0  # compteur de cycles d’horloge

    while p or any(sous_liste for sous_liste in liste_files):
        cycle += 1

        print(f"\n===== Cycle {cycle} =====")

        if not p:
            # Aucun processus en cours : on en prend un nouveau
            p = prioritaire(liste_files)
            if p:
                print(f"Nouveau processus en cours : P{p.PID} (priorité {p.priorite})")
            continue

        # Si le processus en cours est terminé
        if p.temps_utilisation >= p.temps_CPU:
            print(f"P{p.PID} terminé après {p.temps_utilisation} cycles CPU.")
            p = None
            continue

        # Le processus consomme un cycle CPU
        p.temps_utilisation += 1
        print(f"Exécution : P{p.PID} (prio {p.priorite}) [{p.temps_utilisation}/{p.temps_CPU}]")

        # Vérification des files pour une éventuelle préemption
        m = meilleure_priorite(liste_files)
        if m is not None and m <= p.priorite:
            print(f"Préemption : un processus de priorité {m} est en attente.")
            p.priorite = min(p.priorite + 1, len(liste_files) - 1) # min s'assure que le maximum de priorité (3) ne soit pas dépassé
            liste_files[p.priorite].append(p)
            p = prioritaire(liste_files)
            if p:
                print(f"Nouveau processus élu : P{p.PID} (priorité {p.priorite})")
        else:
            # Le processus continue, mais sa priorité baisse légèrement
            p.priorite = min(p.priorite + 1, len(liste_files) - 1)

    print(f"\nSimulation terminée en {cycle} cycles totaux.")
    return cycle


# --- Lancement de la simulation ---
gerer(None, liste_files)
