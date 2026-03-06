from schemas.v1.requests.deduction_request import DeductionSchema
from services.deduction.deduction import Deduction
from services.deduction.dependents_deduction import DependentsDeduction
from services.deduction.education_expenses_deduction import EducationExpensesDeduction
from services.deduction.family_expenses_deduction import GeneralFamilyExpensesDeduction
from services.deduction.health_expenses_deduction import HealthExpensesDeduction


class DeductionFactory:
    
    def __init__(self, context : dict):
        self.context = context

    def execute(self, request : DeductionSchema) -> dict:

        deductions_data = request.model_dump(exclude_none=True)
        print("Dados para cálculo: ", deductions_data)
        expenses = {}
        total = 0
    
        for sub in Deduction.__subclasses__():
            deduction = sub()
            result = deduction.calculate(request, self.context)
            expenses[deduction.key] = result
            total += result
 
        expenses['total'] = total
        return expenses
    
        
            

        
      