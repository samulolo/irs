from services.deduction.deduction import Deduction
from schemas.v1.loader.irs_context import IRSContext
from schemas.v1.requests.deduction_request import DeductionSchema

class DependentsDeduction(Deduction):
    
    key = "dependents"
   
    def calculate(self, dependents : DeductionSchema, context : IRSContext):
        dep = context.deduction(self.key)

        if dependents.dependents.total < 0:
            raise ValueError("O número de dependentes não pode ser um valor negativo")
        
        deduction = dep.get("kids") * dependents.dependents.total  #Garante os 600 para cada dependente.

        eligible_for_300 = max((
            dependents.dependents.dependents_upto_3 +
            dependents.dependents.dependents_upto_6) - 1, 0)
      
        deduction += dependents.dependents.dependents_upto_3 * context.deductions['education']['upto_3']
        deduction += eligible_for_300 * context.deductions['education']['upto_6']

        
        return deduction

    