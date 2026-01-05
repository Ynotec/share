import sys

class BellmanFordSolver:
    
    def __init__(self):
        self.edges = []  # Liste de tuples (u, v, w)
        self.nodes = set() # Ensemble des sommets V
        self.distances = {} # d[v] [cite: 113]
        self.predecessors = {} # pi[v] [cite: 116]
        self.source = None

    def load_graph(self, file_path):
        """
        Lecture du fichier et construction de la structure de graphe.
        Format: noeud_depart noeud_arrivee poids
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    parts = line.strip().split()
                    if not parts: continue # Ignorer lignes vides
                    
                    if len(parts) != 3:
                        print(f"Attention: Format incorrect ligne {line_num} ignorée.")
                        continue
                        
                    u, v, w_str = parts
                    try:
                        w = float(w_str) # Poids décimaux ou entiers
                    except ValueError:
                        print(f"Erreur: Poids invalide ligne {line_num}.")
                        continue
                        
                    self.edges.append((u, v, w))
                    self.nodes.add(u)
                    self.nodes.add(v)
            
            if not self.nodes:
                raise ValueError("Le graphe est vide[cite: 288].")
                
        except FileNotFoundError:
            print(f"Erreur fatale: Le fichier '{file_path}' est introuvable.")
            sys.exit(1)
        except Exception as e:
            print(f"Erreur lors de la lecture: {e}")
            sys.exit(1)

    def initialize(self, source_node):
        """Phase d'initialisation."""
        if source_node not in self.nodes:
            print(f"Erreur: Le nœud source '{source_node}' n'existe pas dans le graphe.")
            sys.exit(1)
            
        self.source = source_node
        # d[v] <- +infini, pi[v] <- NIL
        for node in self.nodes:
            self.distances[node] = float('inf')
            self.predecessors[node] = None
        
        # d[s] <- 0
        self.distances[self.source] = 0

    def solve(self):
        """
        Exécute l'algorithme de Bellman-Ford.
        Retourne False si un cycle négatif est détecté, True sinon.
        """
        num_vertices = len(self.nodes)
        
        # Relaxation itérative (V-1 fois)
        for _ in range(num_vertices - 1):
            changed = False
            for u, v, w in self.edges:
                # Si d[v] > d[u] + w(u,v) 
                if self.distances[u] != float('inf') and \
                   self.distances[v] > self.distances[u] + w:
                    self.distances[v] = self.distances[u] + w
                    self.predecessors[v] = u # pi[v] <- u 
                    changed = True
            
            # Optimisation: Si rien ne change, on arrête ici
            if not changed:
                break
        
        # Détection de cycle négatif
        for u, v, w in self.edges:
            if self.distances[u] != float('inf') and \
               self.distances[v] > self.distances[u] + w:
                return False # Cycle négatif détecté 
                
        return True

    def get_path(self, target):
        """Reconstruit le chemin depuis les prédécesseurs."""
        path = []
        curr = target
        
        # Remonter les prédécesseurs jusqu'à la source
        while curr is not None:
            path.append(curr)
            curr = self.predecessors[curr]
            
            # Prévention contre les boucles infinies
            if len(path) > len(self.nodes) + 1:
                return None 

        return path[::-1] # Inverser pour avoir source -> destination

    def print_results(self, success):
        """ Affiche les résultats. """
        print(f"\nPlus courts chemins depuis le nœud {self.source}:")
        
        if not success:
            print("ALERTE : Un cycle de poids négatif a été détecté accessible depuis la source !")
            return

        sorted_nodes = sorted(list(self.nodes))
        
        for v in sorted_nodes:
            if v == self.source:
                continue
                
            dist = self.distances[v]
            path_list = self.get_path(v)
            
            if dist == float('inf') or path_list is None:
                dist_str = "Inaccessible"
                path_str = "-"
            else:
                dist_str = f"{dist}"
                if dist.is_integer(): 
                    dist_str = f"{int(dist)}" 
                path_str = " -> ".join(path_list)
            
            print(f"Vers {v}: distance = {dist_str}, chemin {path_str}")

def main():
    # Gestion des arguments CLI 
    if len(sys.argv) < 2:
        print("Usage exemple : python bellmanFord.py fichier.txt")
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    solver = BellmanFordSolver()
    solver.load_graph(file_path)
    
    # Choix de la source: argument ou premier nœud par défaut
    source = sys.argv[2] if len(sys.argv) > 2 else sorted(list(solver.nodes))[0]
    
    print(f"Traitement du graphe: {file_path}")
    print(f"Nombre de sommets: {len(solver.nodes)}")
    print(f"Nombre d'arêtes: {len(solver.edges)}")
    
    solver.initialize(source)
    success = solver.solve()
    solver.print_results(success)

if __name__ == "__main__":
    main()