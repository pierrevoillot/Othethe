import UtilitaireDeplacement
class JoueurHumain:
    def __init__(self, couleur):
        self.couleur = couleur
    
    def deplace(self, plateau, deplacementsPossibles):
        deplacements, deplacementChoisi = None, None

        while True:
            try:
                deplacements = input("Entrer les coordonnees de votre deplacement (exemple 2 6 pour [2,6]) : ").split(' ')
                deplacementChoisi = (int(deplacements[0]), int(deplacements[1]))
            except (IndexError, ValueError):
                print("Mauvaise entree ou mauvaises coordonnees")
            else: 
                break

        if deplacementChoisi in deplacementsPossibles:
            UtilitaireDeplacement.mettreAJourPlateau(plateau, deplacementsPossibles, deplacementChoisi, self.couleur)
        else:
           print("Deplacement non autorise ; vous pouvez vous deplacer dans les cases suivantes : ")
           print(list(deplacementsPossibles.keys()))
           self.deplace(plateau, deplacementsPossibles)