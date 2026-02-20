from abc import ABC, abstractmethod

class Deduction(ABC):

    @abstractmethod
    def calculate():
        pass

    def validate_amount(self, amount : float) -> float:
        if amount is None:
            return 0.0
        return max(amount, 0.0)
      