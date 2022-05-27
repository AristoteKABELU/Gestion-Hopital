from Docteur import *
from Patient import *

print("Bienvenue dans le menu!")
liste_patients = []
liste_docteurs = []
dossiers = []   

def main(): 
    """ Notre fonction qui va demarrer notre application """

    while True:
        print("\n Que voulez vous faire: \n \
            1: Enregistrer un Docteur \n \
            2: Enregistrer un patient \n \
            3: Chercher un patient \n \
            4: Chercher un patient a l'aide du Numero dossier \n \
            5: Afficher Tout les patients \n \
            6: Afficher tout les docteurs \n \
            7: Enregistrer plainte \n \
            8: Afficher plainte a l'aide du Numero dossier \n \
            9: Afficher l'IMC a l'aide du Numero dossier \n \
            10: Enregistrer l'horaire de chaque docteur \n \
            11: Vérifié la disponibilité d'un medecin \n \
            12: Quitter le programme \n \
                ")

        try:             # On se rassure que c'est un chiffre qui est tapé
            choix = int(input(""))
        except ValueError:
            print("Veuillez entrer un chiffre Svp !!!")
            continue
        match choix:
            case 1:   # Enregistrement d'un docteur

                nom_docteur = (input("Entrez le nom du Docteur: ")).upper()
                postnom_docteur = (input("Entrez le postnom du docteur: ")).upper()
                prenom_docteur = (input("Entrez le pre-nom du docteur: ")).upper()
                telephone_docteur = input("Entrez le numero de Telephone du docteur: ")
                matricule = generation_matricule(liste_docteurs, nom_docteur, postnom_docteur)
                specialisation = (input("Entrez la specialisiation du docteur: ")).capitalize()
                nouveau_docteur = (enregistrer_un_docteur(
                                                        nom_docteur, postnom_docteur,
                                                        prenom_docteur, telephone_docteur,
                                                        matricule, specialisation))

                # On verifie si le Docteur existe dans la liste!
                nbt = 0
                if liste_docteurs:
                    for i in range(len(liste_docteurs)):
                        if nouveau_docteur[:5] == liste_docteurs[i][:5]:
                            print("Le docteur existe deja! ")
                            nbt += 1

                if nbt == 0:    # Si le Docteur n'y est pas
                    liste_docteurs.append(nouveau_docteur)

            case 2:        # Enregistrement d'un patient

                nom_patient = (input("Entrez le nom du patient: ")).upper()
                postnom_patient = (input("Entrez le postnom du patient: ")).upper()
                prenom_patient = (input("Entrez le pre-nom du patient: ")).upper()
                telephone_patient = input("Entrez le numero de Telephone du patient: ")
                poid_patient = input("Entrez le poid du patients(0.00): ")
                taille_patient = input("Entrez la taille du patient(0.00): ")
                genre_patient = (input("Entrez le genre du patient(M/F): ")).upper()
                age_patient = input("Entrez l'age du patient: ")
                numero_dossier = generer_un_code(dossiers)
                nouveau_patient = (enregistrer_un_patient(
                                                        nom_patient, postnom_patient,
                                                        prenom_patient, telephone_patient,
                                                        poid_patient, taille_patient,
                                                        genre_patient, age_patient, numero_dossier))

                # On verifie si le patient existe dans la liste!
                nbt = 0
                if liste_patients:
                    for i in range(len(liste_patients)):
                        if nouveau_patient[:8] == liste_patients[i][:8]:
                            print("Le patient existe deja! ")
                            nbt += 1
                # Si le patient n'existe pas
                if nbt == 0:
                    liste_patients.append(nouveau_patient)

            case 3:        # Chercher un patient
                if not liste_patients:
                    print("Operation pas encore disponible !")
                else:
                    nom = (input("Entrez le nom du patient que vous cherchez: ")).upper()
                    nbt = 0 # nombre trouve
                    for patient in liste_patients:
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

            case 4:        # Chercher un patient a l'aide du Numero dossier
                if not liste_patients:
                    print("Operation pas encore disponible !")
                else:
                    numero = input("Entrez le numero de dossier du patient: ")
                    for patient in liste_patients:
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

            case 5:        # Afficher Tout les patients
                if not liste_patients:
                    print("Operation pas encore disponible !")
                else:
                    for patient in liste_patients:
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

            case 6:        # Afficher tout les docteurs
                if not liste_docteurs:
                    print("Operation pas encore disponible !")
                else:
                    for docteur in liste_docteurs:
                        print(f"\
                     Nom            : {docteur[0]} \n \
                    Post-nom       : {docteur[1]} \n \
                    Prenom         : {docteur[2]} \n \
                    Telephone      : {docteur[3]} \n \
                    Matricule      : {docteur[4]} \n \
                    Specialisation : {docteur[5]} \n \
                    ____________________________ \
                ")

            case 7:        # Enregistrer plainte
                if not liste_patients:
                    print("Operation pas encore disponible !")

                else:
                    nbt = 0
                    nom_patient = (input("Entrez le nom du patient: ")).upper()

                    for patient in liste_patients:
                        if nom_patient in patient:
                            plainte = (input(f"Entrez la plainte de {patient[0]} {patient[1]} {patient[2]}: ")).lower()
                            enregistrer_plaintes(plainte, patient)
                            nbt += 1

                    if nbt == 0:
                        print(f"{nomPatient} non reconnu dans la liste!")

            case 8:        # Afficher plainte a l'aide du Numero dossier
                if not liste_patients:
                    print("Operation pas encore disponible !")
                else:
                    numero_dossier = input("Entrez le numero dossier du patient: ")
                    for patient in liste_patients:
                        if (numero_dossier == patient[-1] and
                            len(patient) == 10):

                            for plainte in patient[8]:
                                print(f"{patient[0]} {patient[1]} {patient[2]} souffre de {plainte}")

                        elif numero_dossier == patient[-1]:
                            print(f"{patient[0]} {patient[1]} {patient[2]} n'a pas de plainte")

            case 9:        # Afficher l'IMC a l'aide du Numero dossier

                if not liste_patients:
                    print("Operation pas encore disponible !")
                else:
                    numero_dossier = input("Entrez le numero de dossier: ")
                    nbt = 0         # Nombre trouvé
                    
                    for patient in liste_patients:
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

                        nbt += 1

                    if nbt == 0:
                        print("Aucun dossier trouvé!")

            case 10:       # Enregistrer l'horaire de chaque docteur
                if not liste_docteurs:
                    print("Operation pas encore disponible !")
                else:
                    jours = ["lundi", "Mardi", 
                            "Mercredi", "Jeudi",
                            "Vendredi", "Samedi",
                            "Dimanche"]

                for docteur in liste_docteurs:
                    horaire = [] # Horaire de chaque docteur
                    print(f"\t Enregistrement pour le Dr {docteur[0]}!")

                    for jour in jours:
                        reponse = input(f"Etes-vous occupé {jour}?: ")
                        if reponse.lower() == "oui": horaire.append(jour)
                            
                    docteur.append(horaire)

            case 11:       # Vérifié la disponibilité d'un medecin
                        if not liste_docteurs:
                            print("Operation pas encore disponible !")
                        else:
                            nom_docteur = (input("Entrez le nom du medecin: ")).upper()
                            for docteur in liste_docteurs:
                                if (nom_docteur == docteur[0]
                                    or nom_docteur == docteur[1]
                                    or nom_docteur == docteur[2]):

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
                                    print(f"{nomocteur} n'est pas reconnu comme docteur!")

            case 12:       # Quitter le programme
                break
        
main()


