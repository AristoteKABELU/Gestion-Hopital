def chercher_un_patient(liste, nom):

    """ Chercher et afficher un patient a partir de son Nom, Postnom ou Prenom """
      
    nbt = 0 # nombre trouve
    for patient in liste:
        if (nom in patient[0] 
            or nom in patient[1] 
            or nom in patient[2]):

            print(f"\
                     Nom           : {patient[0]} \n \
                    Post-nom      : {patient[1]} \n \
                    Prenom        : {patient[2]} \n \
                    Telephone     : {patient[3]} \n \
                    Poid          : {patient[4]} kg \n \
                    Taille        : {patient[5]} m \n \
                    Genre         : {patient[6]} \n \
                    Age           : {patient[7]} ans \n \
                    Numero Dossier: {patient[8]}  \n")

            nbt += 1
    if nbt == 0: print(f"{nom} non repertorié! ")


def chercher_un_patient_par_numero(numero, liste):

    """ Chercher et afficher un patient a partir de son numero de dossier """

    for patient in liste:
        if numero == patient[-1]:
             print(f"\
                         Nom           : {patient[0]} \n \
                        Post-nom      : {patient[1]} \n \
                        Prenom        : {patient[2]} \n \
                        Telephone     : {patient[3]} \n \
                        Poid          : {patient[4]} kg \n \
                        Taille        : {patient[5]} m \n \
                        Genre         : {patient[6]} \n \
                        Age           : {patient[7]} ans \n \
                        Numero Dossier: {patient[8]}  \n \
                    ")


def afficher_patients(liste):

    """ afficher l'ensemble de patient dans la liste des patients """

    for patient in liste:
        if len(patient) == 9:
            # si le patient n'a pas de plainte
            print(f"\
                         Nom           : {patient[0]} \n \
                        Post-nom      : {patient[1]} \n \
                        Prenom        : {patient[2]} \n \
                        Telephone     : {patient[3]} \n \
                        Poid          : {patient[4]} kg \n \
                        Taille        : {patient[5]} m \n \
                        Genre         : {patient[6]} \n \
                        Age           : {patient[7]} ans \n \
                        Numero Dossier: {patient[8]}  \n \
                        ____________________________ \
                    ")
        else:
             print(f"\
                         Nom           : {patient[0]} \n \
                        Post-nom      : {patient[1]} \n \
                        Prenom        : {patient[2]} \n \
                        Telephone     : {patient[3]} \n \
                        Poid          : {patient[4]} kg \n \
                        Taille        : {patient[5]} m \n \
                        Genre         : {patient[6]} \n \
                        Age           : {patient[7]} ans \n \
                        Plaintes      : {patient[8]} \n \
                        Numero Dossier: {patient[9]}  \n \
                        ____________________________ \
                    ")


def afficher_docteurs(liste):

    """ Afficher les docteurs dans la liste de docteurs """

    for docteur in liste:
        print(f"\
                     Nom            : {docteur[0]} \n \
                    Post-nom       : {docteur[1]} \n \
                    Prenom         : {docteur[2]} \n \
                    Telephone      : {docteur[3]} \n \
                    Matricule      : {docteur[4]} \n \
                    Specialisation : {docteur[5]} \n \
                    ____________________________ \
                ")


def afficher_plainte_patient_via_numero(numero_dossier, liste):

    """ Afficher les plaintes d'un patient a partir de son numero de dossier """

    for patient in liste:
        if (numero_dossier == patient[-1] and
            len(patient) == 10):

            for plainte in patient[8]:
                print(f"{patient[0]} {patient[1]} {patient[2]} souffre de {plainte}")

        elif numeroDossier == patient[-1]:
            print(f"{patient[0]} {patient[1]} {patient[2]} n'a pas de plainte")


def afficher_imc_avec_numero_dossier(numero_dossier, liste):

    """ Afficher l'IMC a partir du numero de dossier d'un patient """

    for patient in liste:
        if numero_dossier == patient[-1]:

            #on essaie de caster nos valeurs
            try:
                poid_patient = float(patient[4])
                taille = float(patient[5])
            except TypeError:
                print("La taille ou le poid, n'est pas bien inscrit!")
                continue

            taille = taille ** 2
            imc = poid_patient / taille

            if imc < 18.5:
                print("Insuffisance normale")
            elif (imc >= 18.5) and (imc <= 25):
                print("Corpulence normale")
            elif (imc > 25) and (imc <=30):
                print("Surpoids")
            elif (imc > 30) and (imc <= 35):
                print("Obéisité modéréé ")
            elif (imc > 35) and (imc <= 40):
                print("Obésité sévère")
            else:
                print("Obésité ,orbite ou massive")


def verifie_disponibilite_docteur(nom_docteur, liste):

    """ Check la disponibilite d'un docteur en particulier dans la semaine 
            a l'aide de son (nom, postnom ou prenom)
    """

    for docteur in liste:
        if (nom_docteur == docteur[0]
            or nomDocteur == docteur[1]
            or nomDocteur == docteur[2]):

            if len(docteur) < 7:
                print("Horaire non etabli !")

            else:
                if len(docteur[-1] < 7):
                    print("Voici le jour qui ne sont pas disponible ")

                    for jour in docteur[-1]:
                        print(f"{jour}", end=" ")

                    rdv = input("\n Veuillez prendre rendez-vous un jour qui n'est pas mentionné: ")
                    if rdv in docteur[-1]:
                        print("Jour deja occupé")

                    elif rdv not in ["lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]:
                        print(f"Désolé {rdv} n'est pas un jour de la semaine!")

                    else:    
                        docteur[-1].append(rdv)

                else:
                    print(f"Monsieur {docteur[0]} n'est pas disponible cette semaine!")
        else:
            print(f"{nomDocteur} n'est pas reconnu comme docteur!")
