from .mindsdb_client import get_server

server = get_server()

def customeProjectName(projectName: str):
    try:
        project = server.create_project(projectName)
        return project
    except Exception as e:
        raise RuntimeError(f"Erreur création projet: {e}")

def customeModelName(projectName: str, modelName: str, window: int, horizon: int):
    try:
        project = server.get_project(projectName)
        model = project.models.create(
        modelName,
        predict='montant_journalier',
        engine= 'neuralforecast',
        query='SELECT * FROM sigfp_source.ml_tresorerie',
                timeseries_options={
                'order': 'journalier',
                'group': 'rubrique',
                'window': window,
                'horizon': horizon
                }
        )
        return model
    except Exception as e:
        raise RuntimeError(f"Erreur création modèle: {e,}")
    
def list_models(project_name: str):
    project = server.get_project(project_name)
    # Liste tous les modèles du projet
    models = project.models.list()  # Renvoie une liste d'objets Model
    
    result = []
    for m in models:
        d = getattr(m, "data", {})
        result.append({
            "name": d.get("name"),
            "engine": d.get("engine"),
            "status": d.get("status"),
            "accuracy": d.get("accuracy"),
            "predict": d.get("predict"),
            "created_at": d.get("created_at"),
            "error": d.get("error"),
            "update_status": d.get("update_status"),
            "version": d.get("version")
        })
    return result
