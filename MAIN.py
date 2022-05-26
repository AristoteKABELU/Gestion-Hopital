from Docteur import *
from Patient import *
from Gestion import *

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
                matricule = input("Entrez le matricule du Docteur: ")
                specialisation = (input("Entrez la specialisiation du docteur: ")).capitalize()
                nouveau_docteur = (enregistrer_un_docteur(
                                                        nom_docteur, postnom_docteur,
                                                        prenom_docteur, telephone_docteur,
                                                        matricule, specialisation))

                # On verifie si le Docteur existe dans la liste!
                nbt = 0
                if liste_docteurs:
                    for i in range(len(liste_docteurs)):
                        if nouveauDocteur[:5] == liste_docteurs[i][:5]:
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
                        if nouveauPatient[:8] == liste_patients[i][:8]:
                            print("Le patient existe deja! ")
                            nbt += 1
                # Si le patient n'existe pas
                if nbt == 0:
                    liste_patients.append(nouveau_patient)


            case 3:       #Chercher un patient
                if not liste_patients:
                    print("Operation pas encore disponible !")
                else:
                    nom = (input("Entrez le nom du patient que vous cherchez: ")).upper()
                    chercher_un_patient(liste_patients, nom)

            case 4:        # Chercher un patient a l'aide du Numero dossier
                if not liste_patients:
                    print("Operation pas encore disponible !")
                else:
                    numero = input("Entrez le numero de dossier du patient: ")
                    chercher_un_patient_par_numero(numero, liste_patients)

            case 5:        #Afficher Tout les patients
                if not liste_patients:
                    print("Operation pas encore disponible !")
                else:
                    afficher_patients(liste_patients)

            case 6:        #Afficher tout les docteurs
                if not liste_docteurs:
                    print("Operation pas encore disponible !")
                else:
                    afficher_docteurs(liste_docteurs)

            case 7:        #Enregistrer plainte
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

            case 8:            #Afficher plainte a l'aide du Numero dossier
                if not liste_patients:
                    print("Operation pas encore disponible !")
                else:
                    numero_dossier = input("Entrez le numero dossier du patient: ")
                    afficher_plainte_patient_via_numero(numero_dossier, liste_patients)

            case 9:            #Afficher l'IMC a l'aide du Numero dossier

                if not liste_patients:
                    print("Operation pas encore disponible !")
                else:
                    numero_dossier = input("Entrez le numero de dossier: ")
                    nbt = 0         # Nombre trouvé
                    for patient in liste_patients:
                        if numeroDossier in patient:
                            afficher_IMC_avec_numero_dossier(numero_dossier, liste_patients)
                            nbt += 1

                    if nbt == 0:
                        print("Aucun dossier trouvé!")

            case 10:       # Enregistrer l'horaire de chaque docteur
                if not liste_docteurs:
                    print("Operation pas encore disponible !")
                else:
                    enregistrer_horaire_docteur(liste_docteurs)

            case 11:       # Vérifié la disponibilité d'un medecin
                if not liste_docteurs:
                    print("Operation pas encore disponible !")
                else:
                    nom_docteur = (input("Entrez le nom du medecin: ")).upper()
                    verifie_disponibilite_docteur(nom_docteur, liste_docteurs)


            case 12:       #Quitter le programme

                print("Vos données ont été enregistré avec succès!")
                break
        
main()


# JE VIENS D'AJOUTER UN COMMENTAIRE ! ! ! !


