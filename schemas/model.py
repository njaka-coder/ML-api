from pydantic import BaseModel
from typing import Optional, List

class CreateModelRequest(BaseModel):
    projectName: str
    modelName: str
    window: int
    horizon: int

class CreateModelResponse(BaseModel):
    status: str
    message: str
    model: str | None = None  # ou autre type/object si tu veux détailler

class ModelInfo(BaseModel):
    name: Optional[str]
    status: Optional[str]
    engine: Optional[str]
    created_at: Optional[str]

class ListModelsResponse(BaseModel):
    models: List[ModelInfo]

