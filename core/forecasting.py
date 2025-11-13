from .mindsdb_client import get_server

def get_prediction(projectName:str, modelName:str, rubrique: str, horizon: int):
    server = get_server()
    project = server.get_project("mindsdb")

    query = f"""
        SELECT m.journalier, m.montant_journalier, m.rubrique
        FROM sigfp_source.ml_tresorerie AS t
        JOIN {projectName}.{modelName} AS m
        WHERE t.rubrique = '{rubrique}'
        LIMIT {horizon};
    """

    result = project.query(query)

    try:
        data = result.fetch()  # DataFrame pandas
        print("✅ Étape 1 : fetch() OK")
        print(data)

        #  Conversion du DataFrame → liste de dictionnaires
        predictions = data.to_dict(orient="records")

        return predictions

    except Exception as e:
        print(f" Erreur lors du fetch: {e}")

        if hasattr(result, "rows") and result.rows:
            return {"predictions": result.rows}

        elif hasattr(result, "data") and result.data:
            return {"predictions": result.data}

        else:
            return {"error": f"Impossible de lire le résultat: {str(e)}"}
