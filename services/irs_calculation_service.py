from services.irs_assessment_service import IrsAssessmentService
from services.taxable_income_calculator import TaxableIncomeCalculator
from schemas.v1.requests.IRSCalculationRequest import IRSCalculationRequestSchema
from schemas.v1.responses.irs_calculation_response import IRSCalculationResponseSchema
from schemas.v1.responses.deductions_response import DeductionsResponseSchema
from schemas.v1.responses.tax_rates_schema import TaxRatesSchema
from services.deduction.deduction_factory import DeductionFactory
from services.irs.irs_loader_service import IRSDataLoaderService
from schemas.v1.loader.irs_context import IRSContext


class IrsCalculationService:

    def __init__(self):
        self.irs_assessment_service = IrsAssessmentService()
        self.taxable_income_servce = TaxableIncomeCalculator()
     
        
    def calculate(self, request : IRSCalculationRequestSchema, context : IRSContext):
        taxable_income = self.taxable_income_servce.calculate(request.gross_income, request.profissional_order)
        colet, tax, bracket, marginal_fee = self.irs_assessment_service.calculate(taxable_income)
       
        deduction_factory = DeductionFactory(context=context)
        deductions = deduction_factory.execute(request.deductions)

        total_deduction = deductions["total"]
        net_colet = colet - total_deduction

        return IRSCalculationResponseSchema(
            taxable_income=taxable_income,
            net_tax=net_colet,
            irs_bracket=bracket,
            tax_rates=TaxRatesSchema(average=tax,marginal=marginal_fee),
            deductions=DeductionsResponseSchema(**(deductions)))
