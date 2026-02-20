
class TotalDeductionsCalculator:

    def __init__(self, deductions : list = []):
        self.deductions = deductions

    def calculate_total(self) -> float:
        return sum(self.deductions)
