import sys

def mettreAJourPlateau(plateau, deplacementsPossibles, deplacementChoisi, couleur):
    piecesToBeCaptured = deplacementsPossibles[deplacementChoisi]
    for (coordonneeX, coordonneeY) in piecesToBeCaptured:
        plateau[coordonneeX][coordonneeY] = couleur
    plateau[deplacementChoisi[0]][deplacementChoisi[1]] = couleur

def genererDeplacementsPossibles(plateau, tour):
	resultatDuDeplacement = {}
	for i in range(8):
		for j in range(8):
			if plateau[i][j] != ' ':
				continue
			else:
				casesEnregistrees = []
				for directionCardinale in getDirections():
					[newX, newY] = [i + directionCardinale[0], j + directionCardinale[1]]
					if dansLimite([newX, newY]) and plateau[nouveauX][nouveauY] != ' ' and plateau[nouveauX][nouveauY] != tour:
						temp = []
						while dansLimite([nouveauX, nouveauY]) and plateau[nouveauX][nouveauY] != ' ' and plateau[nouveauX][nouveauY] != tour:
							temp.append((nouveauX, nouveauY))
							nouveauX += directionCardinale[0]
							nouveauY += directionCardinale[1]
						if dansLimite([nouveauX, nouveauY]) and plateau[nouveauX][nouveauY] == tour:
							casesEnregistrees.extend(temp)
				if len(casesEnregistrees) != 0:
					resultatDuDeplacement[(i,j)] = casesEnregistrees
	return resultatDuDeplacement

def getScore(plateau, couleurJoueurX, couleurJoueurY, N):
    compteurX = 0
    compteurY = 0
    for i in range(N):
        for j in range(N):
            if plateau[i][j] == couleurJoueurX:
                compteurX += 1
            elif plateau[i][j] == couleurJoueurY:
                compteurY += 1
    return (compteurX, compteurY)

def dansLimite(coordonnee):
	return coordonnee[0] >= 0 and coordonnee[0] <= 7 and coordonnee[1] >= 0 and coordonnee[1] <=7

def getDirections(): 
	return [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
