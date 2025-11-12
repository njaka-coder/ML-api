from pydantic import BaseModel

class PredictionInput(BaseModel):
    rubrique: str
    horizon: int

class PredictionOut(BaseModel):
    predictions: list

