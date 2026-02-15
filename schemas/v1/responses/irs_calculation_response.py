from pydantic import BaseModel, field_validator
from schemas.v1.responses.deductions_response import DeductionsResponseSchema
from schemas.v1.responses.tax_rates_schema import TaxRatesSchema



class IRSCalculationResponseSchema(BaseModel):
    taxable_income: float
    net_tax : float
    irs_bracket: float
    tax_rates: TaxRatesSchema
    deductions: DeductionsResponseSchema

    