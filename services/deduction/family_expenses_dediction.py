from services.deduction.deduction import Deduction

class GeneralFamilyExpensesDeduction(Deduction):

    FEE = 0.35
    LIMIT = 250.0 # esse valor é por cada sujeto passivo do agregado familiar ou seja pessoas que entregam declaração de IRS
    def calculate(self, amount : float) -> float:
        amount = self.validate_amount(amount)
        discount = amount * self.FEE
        return min(discount, self.LIMIT)