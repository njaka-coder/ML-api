from pydantic import BaseModel

class CreateModelRequest(BaseModel):
    projectName: str
    modelName: str
    window: int
    horizon: int

class CreateModelResponse(BaseModel):
    status: str
    message: str
    model: str | None = None  # ou autre type/object si tu veux détailler
