from pydantic import BaseModel


class DependentsSchema(BaseModel):
    total : int = 0
    dependents_upto_3: int = 0      # idade ≤ 3 anos
    dependents_upto_6: int = 0      # idade ≤ 6 anos (2.º e seguintes)
