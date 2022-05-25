import random

def enregistrer_un_patient(nom_patient, postnom_patient, prenom_patient,
                            telephone_patient, poid_patient, taille_patient,
                            genre_patient, age_patient, numero_dossier):

    """ Enregistrement d'un patient dans une liste(patient) """

    patient = [nom_patient, postnom_patient, prenom_patient, telephone_patient, poid_patient,
               taille_patient, genre_patient, age_patient, numero_dossier]
    return patient


def generer_un_code(dossier):

    """ Generation code de dossier patient qui sera enregistré dans une liste """

    chiffres = "0123456789"
    numero = random.sample(chiffres,8)
    numero = "".join(numero)
    while numero in dossier:
        # tant que le code est attribué, on re-genere
        chiffres = "0123456789"
        numero = random.sample(chiffres,8)
        numero = "".join(numero)
    return numero


def enregistrer_plaintes(plainte, patient):
    
    """ Enregistrement de plainte d'un patient """

    plaintes = ""
    if len(plainte) > 1:
        if len(patient) == 9:
            plaintes += plainte
            patient.insert(8, plaintes)
        else:
            patient[8] += ", "+plainte



