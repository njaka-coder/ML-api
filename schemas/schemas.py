from pydantic import BaseModel

class PredictionInput(BaseModel):
    projectName: str
    modelName: str
    rubrique: str
    horizon: int

class PredictionOut(BaseModel):
    predictions: list

