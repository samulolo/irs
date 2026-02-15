from services.deduction.deduction import Deduction

class DependentsDeduction(Deduction):
    
    DEPENDE_DEDUTION_AMOUNT = 600 
    ASCENDENT_DEDUTION_AMOUNT = 525

    def calculate(self, dependents : int, ascendent : int = 0):
        if dependents < 0:
            raise ValueError("O número de dependentes não pode ser um valor negativo")
        
        return dependents * self.DEPENDE_DEDUTION_AMOUNT

    