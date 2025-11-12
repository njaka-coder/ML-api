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
