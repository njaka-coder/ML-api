from fastapi import APIRouter
from schemas.schemas import PredictionInput, PredictionOut
from schemas.project import CreateProjectRequest, CreateProjectResponse
from schemas.model import CreateModelRequest, CreateModelResponse,ListModelsResponse,ModelInfo
from core.forecasting import get_prediction
from core.create_project import customeProjectName,customeModelName, list_models

router = APIRouter()
@router.get("/")
async def root():
    return {"message": "Hello World"}
@router.post("/predict", response_model=PredictionOut)
def predict(req: PredictionInput):
    preds = get_prediction(req.projectName,req.modelName,req.rubrique, req.horizon)
    return {"predictions": preds}

@router.post("/create_project", response_model=CreateProjectResponse)
def create_project_api(req: CreateProjectRequest):
    try:
        project = customeProjectName(req.projectName)
        return {"status": "success", "message": f"Projet '{req.projectName}' créé.", "project": str(project)}
    except Exception as e:
        return {"status": "error", "message": str(e), "project": None}

@router.post("/create_model", response_model=CreateModelResponse)
def create_model_api(req: CreateModelRequest):
    try:
        model = customeModelName(req.projectName, req.modelName, req.window, req.horizon)
        return {"status": "success", "message": f"Modèle '{req.modelName}' créé dans '{req.projectName}'.", "model": str(model)}
    except Exception as e:
        return {"status": "error", "message": str(e), "model": None}
    
@router.get("/models/{project_name}", response_model=ListModelsResponse)
def api_list_models(project_name: str):
    try:
        models = list_models(project_name)
        # Normalement, models est une liste de dicts; on les convertit en objets ModelInfo si nécessaire
        return {"models": [ModelInfo(**m) for m in models]}
    except Exception as e:
        # Gérer proprement l’erreur et retourner un message clair
        return {"models": []}
