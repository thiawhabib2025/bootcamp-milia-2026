import numpy as np

# Notes des étudiants
# Chaque ligne représente un étudiant
# Chaque colonne représente une matière :
# Python, Maths, Algèbre

notes = np.array([
    [15, 8, 11],
    [11, 12, 16],
    [17, 14, 13],
    [11, 19, 9],
    [18, 15, 13],
    [7, 8, 11]
])

# Nombre d'étudiants et de matières
print("Forme du tableau :", notes.shape)

# Moyenne de chaque étudiant
moyennes_etudiants = np.mean(notes, axis=1)
print("Moyennes des étudiants :", moyennes_etudiants)

# Moyenne de chaque matière
moyennes_matieres = np.mean(notes, axis=0)
print("Moyennes des matières :", moyennes_matieres)

# Meilleure note de la classe
meilleure_note = np.max(notes)
print("Meilleure note :", meilleure_note)

# Plus petite note de la classe
plus_petite_note = np.min(notes)
print("Plus petite note :", plus_petite_note)

# Transformation du tableau en une dimension
notes_aplaties = notes.flatten()
print("Notes aplaties :", notes_aplaties)