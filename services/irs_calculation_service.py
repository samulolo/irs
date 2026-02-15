from services.irs_assessment_service import IrsAssessmentService
from services.taxable_income_calculator import TaxableIncomeCalculator
from schemas.v1.requests.IRSCalculationRequest import IRSCalculationRequestSchema
from services.deduction.dependents_deduction import DependentsDeduction
from utils.total_deduction import TotalDeductionsCalculator
from schemas.v1.responses.irs_calculation_response import IRSCalculationResponseSchema
from schemas.v1.responses.deductions_response import DeductionsResponseSchema
from schemas.v1.responses.tax_rates_schema import TaxRatesSchema




class IrsCalculationService:

    def __init__(self):
        self.irs_assessment_service = IrsAssessmentService()
        self.taxable_income_servce = TaxableIncomeCalculator()
        self.dependents_deduction = DependentsDeduction()

        
    def calculate(self, request : IRSCalculationRequestSchema):
        taxable_income = self.taxable_income_servce.calculate(request.gross_income, request.profissional_order)
        colet, tax, bracket, marginal_fee = self.irs_assessment_service.calculate(taxable_income)
        
       
        deductions = [
            self.dependents_deduction.calculate(request.depenedents)
        ]
        total_deductions = TotalDeductionsCalculator(deductions)
        total = total_deductions.calculate_total()

        net_colet = colet - total
  
        return IRSCalculationResponseSchema(
            taxable_income=taxable_income,
            net_tax=net_colet,
            irs_bracket=bracket,
            tax_rates=TaxRatesSchema(average=tax,marginal=marginal_fee),
            deductions=DeductionsResponseSchema())
