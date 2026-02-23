from pydantic import BaseModel
from schemas.v1.requests.dependents_request import DependentsSchema


class DeductionSchema(BaseModel):
    dependents: DependentsSchema
    health: float
    family: float
    education: float