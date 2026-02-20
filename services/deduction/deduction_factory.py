from services.deduction.dependents_deduction import DependentsDeduction
from services.deduction.education_expenses_deduction import EducationExpensesDeduction
from services.deduction.health_expenses_deduction import HealthExpensesDeduction
from services.deduction.family_expenses_dediction import GeneralFamilyExpensesDeduction
from schemas.v1.requests.deduction_request import DeductionSchema
from services.deduction.total_deduction import TotalDeductionsCalculator


class DeductionFactory:
    
    def __init__(self):

        self.deductions = {
            "dependents": DependentsDeduction(),
            "health": HealthExpensesDeduction(),
            "family": GeneralFamilyExpensesDeduction(),
            "education": EducationExpensesDeduction()
        }

    def execute(self, request : DeductionSchema) -> dict:
      
        deductions_data = request.model_dump(exclude_none=True)
        expenses = {}
        total = 0

        for key, obj in self.deductions.items():
            
            if key in deductions_data:
                value = deductions_data[key]
                result = obj.calculate(value)
                expenses[key] = result
                total += result
        expenses['total'] = total
        return expenses
    
        
            

        
      