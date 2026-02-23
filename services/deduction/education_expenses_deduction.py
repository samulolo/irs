from services.deduction.deduction import Deduction
from schemas.v1.loader.irs_context import IRSContext
from schemas.v1.requests.deduction_request import DeductionSchema

class EducationExpensesDeduction(Deduction):

    key = "education"
    LIMIT = 800
    FEE = 0.3

    def calculate(self, deduction : DeductionSchema, context : IRSContext) -> float:
        ctx = context.deduction(self.key)
        amount = self.validate_amount(deduction.education)
        discount = ctx.get("tax") * amount
        return min(ctx.get("limit"), discount)

