

class CalculateProfissionalOrder:

    def __init__(self):
        self.order_tax = 0.01
    
    def calculate(self, gross_income : float, value_descounted : float):
        one_porcent_of_gross = self.order_tax * gross_income
        return  min(one_porcent_of_gross, value_descounted)
    