import datetime

def enregistrer_un_docteur(nom_docteur, postnom_docteur, prenom_docteur,
                            telephone_docteur, matricule, specialisation ):

    """" Enregistrement d'un docteur dans une liste(docteur) """

    docteur = [nom_docteur, postnom_docteur, prenom_docteur, telephone_docteur, matricule, specialisation]

    return docteur 
    
def generation_matricule(liste_docteur, nom_docteur, postnom):
    numero = len(liste_docteur) + 1
    numero = str(numero).zfill(3)
    year = str(datetime.datetime.now().year)
    matricule = year[:2] + nom_docteur[0] + postnom[0] + numero
    return matricule