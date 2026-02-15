from pydantic import BaseModel


class DeductionsResponseSchema(BaseModel):
    
    dependents: float = 0.0
    ascendants: float = 0.0
    general_expenses: float = 0.0
    education: float = 0.0
    health: float = 0.0
    total: float = 0.0
