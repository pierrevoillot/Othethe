from UtilitaireDeplacement import genererDeplacementsPossibles, getScore
import Othello
import sys 

def initialiserJeu(N, experimentation):
    if experimentation:
        return initialisationPlateau(N), 'N', 'B', True
    else:
        couleurJoueur1 = input("Choisissez la couleur du joueur 1 (B pour Blanc, N pour Noir) : ")
        while couleurJoueur1 != 'N' and couleurJoueur1 != 'B':
            couleurJoueur1 = input("Choisissez la couleur du joueur 1 (B pour Blanc, N pour Noir) : ")
        couleurJoueur2 = 'N' if couleurJoueur1 == 'B' else 'B'
        print("Joueur 1 est %s" % couleurJoueur1)
        print("Joueur 2 est %s" % couleurJoueur2)
        tourJoueur1 = (couleurJoueur1 == 'N') 
        print("Le joueur ayant les pions Noirs commence")
        return initialisationPlateau(N), couleurJoueur1, couleurJoueur2, tourJoueur1 

def initialisationPlateau(N):
    plateau = []
    for x in range(N):
        plateau.append([' '] * N)

    plateau[3][3] = 'B'
    plateau[4][4] = 'B'
    plateau[3][4] = 'N'
    plateau[4][3] = 'N'
    return plateau 

def dessinerPlateau(plateau, N, score, tourJoueur1):
    
    HORIZONTALE = '  +---+---+---+---+---+---+---+---+'
    VERTICALE = '  |   |   |   |   |   |   |   |   |'

    print('    0   1   2   3   4   5   6   7')
    print(HORIZONTALE)
    for y in range(N):
        print(y, end =" ")
        for x in range(N):
            print('| %s' % (plateau[x][y]), end=" ")
        print('|')
        print(HORIZONTALE)

def jouerPartie(N, plateau, joueur1, joueur2, tourJoueur1, experimentation):
    gagnant = None

    while True:
        if not experimentation:
            if tourJoueur1:
                print("Tour du joueur 1!")
            else:
                print("Tour du joueur 2!") 
            
            scoreActuel = getScore(plateau, joueur1.couleur, joueur2.couleur, N)
            print("Score actuel : Joueur 1 : %s vs Joueur 2 : %s" % (scoreActuel[0], scoreActuel[1]))

            dessinerPlateau(plateau, N, scoreActuel, tourJoueur1)
           
        joueur1PeutDeplacer, joueur1SeDeplace = peutSeDeplacer(plateau, joueur1.couleur)
        joueur2PeutDeplacer, joueur2SeDeplace = peutSeDeplacer(plateau, joueur2.couleur)
        
        if not (joueur1PeutDeplacer or joueur2PeutDeplacer):
            if not experimentation: dessinerPlateau(plateau, N, scoreActuel, None)
            gagnant = finJeu(joueur1.couleur, joueur2.couleur, plateau, N, experimentation)
            break
        elif tourJoueur1 and joueur1PeutDeplacer:
            joueur1.deplace(plateau, joueur1SeDeplace)
            tourJoueur1 = False
        elif not tourJoueur1 and joueur2PeutDeplacer:
            joueur2.deplace(plateau, joueur2SeDeplace)
            tourJoueur1 = True
        elif not tourJoueur1 and not joueur2PeutDeplacer:
            if not experimentation:
                print("Le joueur 2 ne peut pas bouger ; le tour passe au joueur 1") 
            joueur1.deplace(plateau, joueur1SeDeplace)
        elif tourJoueur1 and not joueur1PeutDeplacer:
            if not experimentation:
                print("Le joueur 1 ne peut pas bouger ; le tour passe au joueur 2")
            joueur2.deplace(plateau, joueur2SeDeplace)
    return gagnant

def peutSeDeplacer(plateau, couleur):
    deplacementsPossibles = genererDeplacementsPossibles(plateau, couleur)
    if len(list(deplacementsPossibles.keys())) == 0:
        return False, deplacementsPossibles
    else:
        return True, deplacementsPossibles


def finJeu(couleurJoueur1, couleurJoueur2, plateau, N, experimentation):
    compteurScore = getScore(plateau, couleurJoueur1, couleurJoueur2, N)
    joueur1Gagne = True if compteurScore[0] > compteurScore[1] else False
    if not experimentation:
        print("Le joueur 1 a un score de %s" % compteurScore[0])
        print("Le joueur 2 a un score de  %s" % compteurScore[1])
        print("%s a gagné!" % ("Joueur 1" if joueur1Gagne else "Joueur 2"))
        recommencer = input("Voulez-vous recommencer une partie (o pour oui, n pour non): ")
        if recommencer == 'o':
            Othello.othello(8, False, None, None)
        else:
            sys.exit(0)
    if joueur1Gagne:
        return couleurJoueur1
    else:
        return couleurJoueur2