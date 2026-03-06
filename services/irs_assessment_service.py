from services.taxable_income_calculator import TaxableIncomeCalculator
from utils.util import format_number
from schemas.v1.loader.irs_context import IRSContext

class IrsAssessmentService:

    def __init__(self):
        self.taxable_income_service = TaxableIncomeCalculator()

    def calculate(self, taxable_income : float, context : IRSContext):
        previous_bracket_value = 0
        remain_value = taxable_income
        coleta = 0
        irs_bracket = 0
        marginal_fee = 0
        irs_bracket = context.irs_brackets

        for bracket in irs_bracket:
            if remain_value <= 0: break
            rendimento_max = bracket['rendimento_max'] if bracket['rendimento_max'] is not None else taxable_income
            current_bracket = min(taxable_income, rendimento_max)
            dif = current_bracket - previous_bracket_value
            coleta += dif * bracket['taxa']
            previous_bracket_value = current_bracket
            remain_value -= dif
            irs_bracket = bracket['escalao']
            marginal_fee = bracket['taxa']

        average_fee = format_number((coleta / taxable_income))
        return coleta , average_fee , irs_bracket , format_number(marginal_fee)



