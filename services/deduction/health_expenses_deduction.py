from services.deduction.deduction import Deduction
from schemas.v1.loader.irs_context import IRSContext
from schemas.v1.requests.deduction_request import DeductionSchema

class HealthExpensesDeduction(Deduction):

    key = "health"

    def calculate(self, deduction : DeductionSchema, context : IRSContext) -> float:
        ctx = context.deduction(self.key)
        amount = self.validate_amount(deduction.health)
        discount = amount * ctx.get("tax")
        return min(ctx.get("limit"), discount)
    