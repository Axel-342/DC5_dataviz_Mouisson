import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Charger le dataset
df = pd.read_csv("dataset_marketing_cleaned.csv")
# 2. Agréger les impressions par campagne
impressions_par_campagne = df.groupby("Campagne")["Impressions"].sum().reset_index()
# 3. Configurer la taille de la figure
plt.figure(figsize=(10, 6))
# 4. Créer un diagramme en barres
sns.barplot(data=impressions_par_campagne, x="Campagne", y="Impressions")
# 5. Personnaliser l'histogramme
plt.title("Histogramme des Impressions par Campagne")
plt.xlabel("Campagne")
plt.ylabel("Nombre total d'Impressions")
plt.xticks(rotation=45)
plt.tight_layout()
# 6. Enregistrer l’histogramme sous forme de fichier PNG
plt.savefig("histogram_impressions.png", dpi=300)  # dpi=300 pour une bonne résolution
# 7. Afficher l’histogramme
plt.show()
