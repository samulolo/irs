from pydantic import BaseModel, field_validator
from exceptions.greater_than_zero_exception import GreaterThanZeroException
from schemas.v1.requests.deduction_request import DeductionSchema


class IRSCalculationRequestSchema(BaseModel):

    gross_income : float
    depenedents : int
    deductions : DeductionSchema
    profissional_order : float


    @field_validator('gross_income', mode="after")
    @classmethod
    def validate_gross_income(cls, value):

        if value is None or value <= 0: 
            raise GreaterThanZeroException("O ordernado bruto é obrigatório, e deve ser maior que zero")
        
        return value
    


    