import os

while True:
    print("\n===== Gestionnaire de fichiers =====")
    print("1. Afficher les fichiers")
    print("2. Créer un dossier")
    print("3. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        print(os.listdir())

    elif choix == "2":
        nom = input("Nom du dossier : ")
        os.makedirs(nom, exist_ok=True)
        print("Dossier créé.")

    elif choix == "3":
        print("Au revoir.")
        break

    else:
        print("Choix invalide.")
