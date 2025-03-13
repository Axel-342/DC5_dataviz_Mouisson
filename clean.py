import pandas as pd

# Charger le fichier
def clean_marketing_data(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Supprimer la colonne inutile
    df_cleaned = df.drop(columns=["Inutile"], errors='ignore')
    
    # Convertir la colonne Date en datetime
    df_cleaned["Date"] = pd.to_datetime(df_cleaned["Date"], errors='coerce')
    
    # Supprimer les lignes avec des valeurs manquantes
    df_cleaned = df_cleaned.dropna()
    
    # Supprimer les valeurs aberrantes
    df_cleaned = df_cleaned[
        (df_cleaned["Clics"] >= 0) &
        (df_cleaned["Conversions"] >= 0) &
        (df_cleaned["Coût"] >= 0) &
        (df_cleaned["Conversions"] < 5000)  # Supposons que 5000 est une limite raisonnable
    ]
    
    # Sauvegarder le fichier nettoyé
    df_cleaned.to_csv(output_file, index=False)
    print(f"Fichier nettoyé enregistré sous : {output_file}")

# Utilisation
input_file = "dataset_marketing_dataviz.csv"
output_file = "dataset_marketing_cleaned.csv"
clean_marketing_data(input_file, output_file)