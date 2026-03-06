

class IRSContext:

    def __init__(self, config : dict):
        self.tax_year = config["tax_year"]
        self.minimum_deductions = config["minimum_deductions"]
        self.deductions = config["deductions"]
        self.irs_brackets = config['irs_brackets']

    def deduction(self, key : str):
        return self.deductions.get(key)