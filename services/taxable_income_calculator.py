from services.social_secutity_calculator import CalculateSocialSecurity
from services.professional_order_calculator import CalculateProfissionalOrder

class TaxableIncomeCalculator:

    MIN_SPECIFIC_DEDUCTION = 4104
    
    def __init__(self):
        self.social_security_service = CalculateSocialSecurity()
        self.profissional_order_service = CalculateProfissionalOrder()

    def calculate(self, gross_Income : float, profess_order : float):
        socialSecurityDescount = self.social_security_service.calculate(gross_Income)
        professional_order = self.profissional_order_service.calculate(gross_income=gross_Income, value_descounted=profess_order)
        specific_dedution = professional_order + socialSecurityDescount
        dedution = max(self.MIN_SPECIFIC_DEDUCTION, specific_dedution)
        return gross_Income - dedution
    


