from copy import deepcopy
from collections import Counter
from DeplacementAleatoireIA import DeplacementAleatoireIA
import UtilitaireDeplacement
import Jeu
import random

class MonteCarloIA:
    def __init__(self, couleur, nombreDeSimulation):
        self.couleur = couleur
        self.couleurOpposant = 'B' if self.couleur == 'N' else 'N'
        self.nombreDeSimulation = nombreDeSimulation

    def deplace(self, plateau, deplacementsPossibles):
        coupLegaux = list(deplacementsPossibles.keys())
        compteur = Counter()
        for coupLegal in coupLegaux:
        	for i in range(int(self.nombreDeSimulation)):
        		copieDuPlateau = deepcopy(plateau)
        		UtilitaireDeplacement.mettreAJourPlateau(copieDuPlateau, deplacementsPossibles, coupLegal, self.couleur)
        		gagnant = Jeu.jouerPartie(8, copieDuPlateau, DeplacementAleatoireIA(self.couleur), DeplacementAleatoireIA(self.couleurOpposant), False, True)
        		if gagnant == self.couleur:
        			compteur[coupLegal] += 1
        deplacementChoisi = compteur.most_common(1)[0][0] if len(compteur) > 0 else random.choice(coupLegaux)
        UtilitaireDeplacement.mettreAJourPlateau(plateau, deplacementsPossibles, deplacementChoisi, self.couleur)
