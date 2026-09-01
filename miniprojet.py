import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Étudiant": ["Ali","Fatou","Moussa","Awa","Ibrahima","Mariama"],
    "Python": [15,12,17,10,14,18],
    "Mathématiques": [14,16,15,11,13,17],
    "Algèbre": [16,13,18,12,15,16],
    "Présence": [95,88,97,75,90,98]
}

df=pd.DataFrame(data)
print(df)

# calcule des moyennes des etudiants

df["moyenne_etd"]=(df["Python"]+df["Mathématiques"]+df["Algèbre"])/3
print(df)
# voire les etudiants qui ont  une moyenne superieure ou egal a 14
idx=df[df["moyenne_etd"]>=14].index
print("Les  etudiants qui ont une moyenne>=14 sont",df.loc[idx])
# le classement
idx_classement=df["moyenne_etd"].sort_values(ascending=False).index
print("le classement est",df.loc[idx_classement])


# verification s il y a une relation entre moyenne et precence 
X=df["moyenne_etd"]
Y=df["Présence"]
plt.scatter(X,Y)
plt.title("nuage de points entre les moyennes et leurs presence")
plt.xlabel("moyennes")
plt.ylabel("precence")
plt.show()
correlation=X.corr(Y)
print("la correlation est:",correlation)



