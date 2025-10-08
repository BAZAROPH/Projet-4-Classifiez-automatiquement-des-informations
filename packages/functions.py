import pandas as pd

def count_row_col(df, name):
    """Fonction permettrant d'afficher le nombre de colonne et de ligne d'un dataframe
    
        ------------
        parameters:
        df: dataframe
        name: Nom du dataframe
    """
    print(f"Pour {name} on a {df.shape[0]} lignes et {df.shape[1]} colonnes")
    
    
def count_na(df, column, result_type="number"):
    """
        Fonction permettant de savoir le pourcentage de valeur manquante d'une colonne

        -----------
        parmeters
        df: Le dataframe
        column: La colonne sur laquelle le calcul doit se faire

        return
        missing_count: Nombre de valeurs manquantes ou pourcentage de valeurs manquantes
    """
    nb_line = df.shape[0]
    missing_count = df[column].isna().sum()
    if(result_type == "percent"):
        return round((missing_count*100)/nb_line, 2)
    return missing_count

def category_descriptive_stat(df, columns):
    """
        Fonction qui retourne l'effectif et la fréquence de chaque feature catégorielle d'un dataframe

        ------------------
        parameters
        df: dataframe,
        columns: les colonnes catégorielle

    """
    for column in columns:
        print(f"Pour la colonne {column}")
        elt = pd.DataFrame({
            "Effectif": df[column].value_counts(dropna=False),
            "Fréquence":  df[column].value_counts(normalize=True, dropna=False)*100
        })
        display(elt)
