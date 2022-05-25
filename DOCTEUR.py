def enregistrer_un_docteur(nom_docteur, postnom_docteur, prenom_docteur,
                            telephone_docteur, matricule, specialisation ):

    """" Enregistrement d'un docteur dans une liste(docteur) """

    docteur = [nom_docteur, postnom_docteur, prenom_docteur, telephone_docteur, matricule, specialisation]

    return docteur 


def enregistrer_horaire_docteur(liste):

    """ Enregistrement de l'horaire de chaque docteur """

    jours = ["lundi", "Mardi", 
            "Mercredi", "Jeudi",
            "Vendredi", "Samedi",
            "Dimanche"]

    for docteur in liste:
        horaire = [] # Horaire de chaque docteur
        print(f"\t Enregistrement pour le Dr {docteur[0]}!")

        for jour in jours:
            reponse = input(f"Etes-vous occupé {jour}?: ")
            if reponse.lower() == "oui": horaire.append(jour)
                
        docteur.append(horaire)