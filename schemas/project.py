from pydantic import BaseModel

class CreateProjectRequest(BaseModel):
    projectName: str

class CreateProjectResponse(BaseModel):
    status: str
    message: str
    project: str 
