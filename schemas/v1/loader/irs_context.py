

class IRSContext:

    def __init__(self, config : dict):
        self.tax_year = config["tax_year"]
        self.minimum_deductions = config["minimum_deductions"]
        self.deductions = config["deductions"]

    def deduction(self, key : str):
        return self.deductions.get(key)