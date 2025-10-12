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
            "Fréquence":  (df[column].value_counts(normalize=True, dropna=False)*100).round(2)
        })
        display(elt)

def categorize_age(age: int):
    """
        Fonction qui permet de catgéoriser une personne dans une tranche d'age en fonction de son age

        ----------
        parameters:
        age: int
            age de l'individu

        returns
            category: string
                tranche d'age de l'individu
    """
    if age <= 30:
        return "Jeune"
    elif age > 30 and age < 43:
        return "Adulte"
    else:
        return "Senior"

def categorize_revenu(revenu: float):
    """
        Fonction qui permet de catégoriser les revenus d'un employé en fonction du montant

        ----------
        parameters:
        revenu: float
            revenu mensuel de l'employé
        returns
            category: string
                catégorie à laquelle appartient le revenu
    """

    if revenu <= 2911:
        return "Bas"
    elif revenu > 2911 and revenu < 8379:
        return "Moyen"
    else:
        return "Élevé"

def type_separator(df: pd.DataFrame, exception:list=[]):
    """
        fonction qui sépare les colonnes catégorielles et numérique d'un data frame

        -----------
        parameters
        df: DataFrame
            jeu de données
        exception: list()
            liste des colonnes à ignorer

        -------
        returns
        features: tuple()
            les colonnes catégorielles et numériques
    """
    numeric = list()
    categorical = list()
    for column in df.columns:
        if column not in exception:
            if df[column].dtype == "int64" or df[column].dtype == "float64":
                numeric.append(column)
            elif df[column].dtype == "object":
                categorical.append(column)
    return (numeric, categorical)



