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
        model = project.create_model(
            modelName,
            predict='montant_journalier',
            query='SELECT * FROM sigfp_source.ml_tresorerie',
            options={
                'engine': 'neuralforecast',
                'order_by': 'journalier',
                'group_by': 'rubrique',
                'window': window,
                'horizon': horizon
            })
        return model
    except Exception as e:
        raise RuntimeError(f"Erreur création modèle: {e,}")
