from pydantic import BaseModel


class TaxRatesSchema(BaseModel):
    average : float = 0.0
    marginal : float = 0.0
