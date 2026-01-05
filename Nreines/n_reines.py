import sys
from pysat.solvers import Glucose3

class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.solver = Glucose3()
        self.clauses = []

    def get_clauses(self):
        return self.clauses
    
    def to_var(self, r, c):
        """
        Le solveur SAT ne fonctionne pas avec le concept case (ligne, colonne), il ne comprend que des 
        nombres entiers positifs (1, 2, 3, ...) qui peut être vrai ou faux.

        Cette fonction permet donc de convertir une position (ligne, colonne) en un entier unique.
        La case (0,0) devient 1, (0,1) devient 2, ..., (1,0) devient n+1, etc.

        Formule : (r * n) + c + 1

        r = ligne
        c = colonne
        n = taille de l'échiquier
        1 est ajouté pour éviter la variable 0.

        r * n : lire r lignes complètes, comme chaque ligne contient n cases, j'ai passé r*n cases au total.
        + c : dans la ligne r, j'avance de c colonnes.
        + 1 : je décalle tout de 1, parce que dans SAT le 0 est réservé pour la fin de ligne et on ne peut pas l'utiliser comme variable.
        """
        return (r * self.n) + c + 1

    def from_var(self, var):
        """
        Cette fonction permet de convertir une variable SAT (entier positif) en une position (ligne, colonne).
        par exemple : si dans mon retour j'ai "La variable 7 est VRAIE", je veux savoir à quelle case cela correspond sur l'échiquier.

        abs(var) - 1 : on enlève 1 pour compenser le +1 fait dans to_var.

        v // self.n : si j'ai la case numéro 6 et que les lignes font 4 cases, je fais 6 // 4 = 1, donc ligne 1.
        v % self.n : si j'ai la case numéro 6 et que les lignes font 4 cases, je fais 6 % 4 = 2, donc colonne 2.
        6 correspond donc à la case (1, 2)
        """
        v = abs(var) - 1
        return (v // self.n, v % self.n)

    def add_clause(self, clause):
        """
        L'argument clause est une liste d'entiers représentant une dicjonction (OR) de littéraux.

        self.solver.add_clause(clause) : ajoute la clause au solveur SAT, il va mémorisé cette contrainte, et ne pourra pas renvoyer une solution qui ne respecte pas cette clause.
        self.clauses.append(clause) : dans la ligne au dessus, on stocke la règle pour le solveur, mais il n'est pas possible de relire les règles plus tard. Donc on les stocke aussi dans une liste locale pour pouvoir les réutiliser si besoin.

        Ce qui permet si jamais il n'y a pas de solution, on peut afficher son contenu pour vérifier si une règle n'a pas été mal formulée ou autre.
        """
        self.solver.add_clause(clause)
        self.clauses.append(clause)

    def generate_constraints(self):
        """
        Étape 1 & 2 : Définition des contraintes et conversion CNF
        """
        print(f"Génération des contraintes pour n={self.n}...")

        # 1. Contrainte d'existence : Au moins une reine par ligne
        # Clause de la forme : (X i,1 OR X i,2 OR .. OR X i,n)
        # Il faut une reine en colonne 1 ou 2 ou ... ou n pour chaque ligne r.
        # for r in range(self.n) : sélectionne la ligne a traiter
        # for c in range(self.n) : on se déplace de gauche à droite à l'intérieur de cette ligne (colonne 1, 2, ..., n))
        for r in range(self.n):
            clause_ligne = []
            for c in range(self.n):
                clause_ligne.append(self.to_var(r, c))
            self.add_clause(clause_ligne)

        # 2. Contraintes d'unicité (Conflits)
        # Nous devons interdire deux reines sur la même ligne, colonne ou diagonale.
        # Règle : (NON Xa OR NON Xb)
        
        # On parcourt chaque case (r1, c1) de l'échiquier
        for r1 in range(self.n):
            for c1 in range(self.n):
                # On compare avec toutes les autres cases (r2, c2)
                # pour éviter les doublons, on regarde seulement les cases suivantes
                for r2 in range(self.n):
                    for c2 in range(self.n):
                        
                        # On saute la comparaison de la case avec elle-même
                        if r1 == r2 and c1 == c2:
                            continue
                        
                        # Pour éviter de générer A vs B puis B vs A, on impose un ordre
                        # On traite seulement si la deuxième case a un index plus grand
                        if self.to_var(r2, c2) <= self.to_var(r1, c1):
                            continue

                        is_conflict = False
                        
                        # Même ligne ?
                        if r1 == r2:
                            is_conflict = True
                        
                        # Même colonne ?
                        if c1 == c2:
                            is_conflict = True
                        
                        # Même diagonale ? 
                        if(abs(r1 - r2) == abs(c1 - c2)):
                            is_conflict = True

                        # Si conflit détecté, on ajoute la clause CNF : (NON A ou NON B)
                        if is_conflict:
                            # En SAT, NON se note avec un signe moins
                            self.add_clause([-self.to_var(r1, c1), -self.to_var(r2, c2)])

    def solve(self):
        """
        Résolution via le solveur SAT
        """
        if self.solver.solve():
            return self.solver.get_model()
        else:
            print("Résolution terminée.")
            return None

    def print_board(self, model):
        """
        Affiche la solution de manière lisible
        """
        if not model:
            return

        # On extrait les variables vraies du modèle
        queens = set()
        for var in model:
            if var > 0:
                queens.add(self.from_var(var))

        print(f"\n=== Échiquier {self.n}x{self.n} {"=" * self.n}\n")
        print("  " + "".join([f"  {c} " for c in range(self.n)]))
        print("  " + "+---" * self.n + "+")
        for r in range(self.n):
            line_str = f"{r} |"
            for c in range(self.n):
                if (r, c) in queens:
                    line_str += " Q |" 
                else:
                    line_str += "   |" 
            print(line_str)
            print("  " + "+---" * self.n + "+")

if __name__ == "__main__":

    choice = input("Entrez la taille de l'échiquier ? : ")
    while choice and not choice.isdigit():
        print("Veuillez entrer un nombre valide.")
        choice = input("Entrez la taille de l'échiquier ? : ")

    if choice:
        n = int(choice)

    print(f"\n=== Recherche de TOUTES les solutions pour N={n} ===")
    
    game = NQueensSolver(n)
    game.generate_constraints()

    compteur = 0
    
    while True:
        solution = game.solve()
        if not solution:
            break 
        
        compteur += 1
        
        # Afficher uniquement la première solution trouvée
        if compteur == 1:
            game.print_board(solution)
        
        # On inverse tous les signes : Si 1 était Vrai, il devient -1 (Faux)
        game.add_clause([-x for x in solution])

    if compteur == 0:
        print(f"Aucune solution trouvée pour N={n}.")
    else:
        print(f"\nNombre total de solutions trouvées pour N={n} : {compteur}")

    
    contraintes = input("Voulez-vous afficher les contraintes ? (o/n) : ")
    if contraintes.lower() == 'o':
        print("Contraintes utilisées :")
        for clause in game.get_clauses():
            print(clause)