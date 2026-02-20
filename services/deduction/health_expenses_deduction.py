from services.deduction.deduction import Deduction

class HealthExpensesDeduction(Deduction):

    LIMIT = 1000.0
    FEE = 0.15
    def calculate(self, amount : float) -> float:
        amount = self.validate_amount(amount)
        discount = amount * self.FEE
        return min(self.LIMIT, discount)
    