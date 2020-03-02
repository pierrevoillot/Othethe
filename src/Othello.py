import Jeu
from JoueurHumain import JoueurHumain
from DeplacementAleatoireIA import DeplacementAleatoireIA
from MonteCarloIA import MonteCarloIA 

def othello(N, experimentation, experimentationJoueur1, experimentationJoueur2):
    print("")
    print("*****************************************************************")
    print("**************************** OTHELLO ****************************")
    print("*****************************************************************")
    print("")
    plateau, couleurJoueur1, couleurJoueur2, tourJoueur1 = Jeu.initialiserJeu(N, experimentation)
    
    if not experimentation:
        print("Vous pouvez decider de jouer ou de laisser l'ordinateur jouer")
        print("")
        print("Veuillez entrer votre option") 
        print("")
        print("\t0 pour jouer")
        print("\t1 pour une IA effectuant des deplacements aleatoires")
        print("\t2 pour une IA effectuant des deplacements avec l'algorithme Monte Carlo")
        print("")
        joueur1 = choixJoueur(input("Entrer votre option pour le joueur 1 : "), couleurJoueur1)
        joueur2 = choixJoueur(input("Entrer votre option pour le joueur 2 : "), couleurJoueur2)
    else: 
        joueur1 = choixJoueur(experimentationJoueur1[0], experimentationJoueur1[1])
        joueur2 = choixJoueur(experimentationJoueur2[0], experimentationJoueur2[1])

    return Jeu.jouerPartie(N, plateau, joueur1, joueur2, tourJoueur1, experimentation)
       
def choixJoueur(option, couleur):
    option = int(option)
    if option == 0:
        return JoueurHumain(couleur)
    elif option == 1:
        return DeplacementAleatoireIA(couleur)
    elif option == 2:
        nombreDeSimulation = input("Entrer le nombre de simulation pour le joueur %s : " % couleur)
        return MonteCarloIA(couleur, nombreDeSimulation)
    else:
        option = input("Veuillez entrer une option valide")
        choixJoueur(option)
        
if __name__ == '__main__':
    othello(8, False, None, None)