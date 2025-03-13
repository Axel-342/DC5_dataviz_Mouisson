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

# 8. Convertir la colonne Date en format datetime
df["Date"] = pd.to_datetime(df["Date"])

# 9. Regrouper les données par jour et par campagne, et sommer les clics
df_grouped = df.groupby([df["Date"].dt.date, "Campagne"])["Clics"].sum().reset_index()

# 10. Configurer la taille de la figure pour l'évolution des clics
plt.figure(figsize=(12, 6))

# 11. Tracer l'évolution des clics par jour
sns.lineplot(data=df_grouped, x="Date", y="Clics")

# 12. Personnaliser le graphique
plt.title("Évolution des Clics par Jour")
plt.xlabel("Date")
plt.ylabel("Nombre de Clics")
plt.xticks(rotation=45)
plt.legend(title="Campagne")
plt.tight_layout()

# 13. Enregistrer le graphique
plt.savefig("evolution_clics_par_jour.png", dpi=300)

# 14. Afficher le graphique
plt.show()

# 15. Créer un scatterplot (Nuage de points) entre Clics et Conversions avec une ligne de régression
plt.figure(figsize=(10, 6))

# 16. Vérifier si la colonne "Conversions" existe
if 'Conversions' in df.columns:
    # Utilisation de sns.regplot pour ajouter une ligne de régression
    sns.regplot(data=df, x="Clics", y="Conversions", scatter_kws={'s': 100}, line_kws={'color': 'red'}, ci=None)
    plt.title("Clics vs Conversions avec Ligne de Régression")
    plt.xlabel("Nombre de Clics")
    plt.ylabel("Nombre de Conversions")
    plt.tight_layout()
    
    # 17. Enregistrer le scatterplot avec la ligne de régression
    plt.savefig("clics_vs_conversions_regression.png", dpi=300)
    
    # 18. Afficher le scatterplot
    plt.show()
else:
    print("La colonne 'Conversions' n'existe pas dans le dataset.")

# 19. Sélectionner uniquement les colonnes numériques pour la corrélation
df_numeric = df.select_dtypes(include=[float, int])

# 20. Calculer la matrice de corrélation
correlation_matrix = df_numeric.corr()

# 21. Créer la heatmap des corrélations
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, cbar=True)

# 22. Personnaliser la heatmap
plt.title("Heatmap des Corrélations")
plt.tight_layout()

# 23. Enregistrer la heatmap sous forme de fichier PNG
plt.savefig("heatmap_correlations.png", dpi=300)

# 24. Afficher la heatmap
plt.show()
