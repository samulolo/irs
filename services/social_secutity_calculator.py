

class CalculateSocialSecurity:

    def __init__(self):
        self.social_security_tax = 0.11

    def calculate(self, gross_income : float):
        return self.social_security_tax * gross_income