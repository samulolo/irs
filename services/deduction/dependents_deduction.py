from services.deduction.deduction import Deduction
from schemas.v1.loader.irs_context import IRSContext
from schemas.v1.requests.deduction_request import DeductionSchema

class DependentsDeduction(Deduction):
    
    key = "dependents"
   
    def calculate(self, dependents : DeductionSchema, context : IRSContext):
        dep = context.deduction(self.key)

        if dependents.dependents.total < 0:
            raise ValueError("O número de dependentes não pode ser um valor negativo")
        
        deduction = dep.get("kids") * dependents.dependents.total #Garante os 600 para cada dependente.
        
        if dependents.dependents.dependents_upto_3 + dependents.dependents.dependents_upto_6 > dependents.dependents.total:
            raise ValueError("As idades não coicidem com o total de dependentes.")

        deduction += dependents.dependents.dependents_upto_3 * 126
        deduction += dependents.dependents.dependents_upto_6 * 300
        
        return deduction

    