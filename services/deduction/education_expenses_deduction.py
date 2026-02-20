from services.deduction.deduction import Deduction

class EducationExpensesDeduction(Deduction):

    LIMIT = 800
    FEE = 0.3

    def calculate(self, amount : float) -> float:
        amount = self.validate_amount(amount)
        discount = self.FEE * amount
        return min(self.LIMIT, discount)

