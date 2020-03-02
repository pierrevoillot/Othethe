import random, UtilitaireDeplacement

class DeplacementAleatoireIA:
    def __init__(self, couleur):
        self.couleur = couleur
    
    def deplace(self, plateau, deplacementsPossibles):
        coupsLegaux = list(deplacementsPossibles.keys())
        mouvementChoisi = random.choice(coupsLegaux)
        UtilitaireDeplacement.mettreAJourPlateau(plateau, deplacementsPossibles, mouvementChoisi, self.couleur)