from pydantic import BaseModel


class DeductionSchema(BaseModel):
    dependents: int
    health: float
    family: float
    education: float