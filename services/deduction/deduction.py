from abc import ABC, abstractmethod

class Deduction(ABC):

    registry: dict[str, type["Deduction"]] = {}

    key: str

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if not hasattr(cls, "key"):
            raise ValueError(f"{cls.__name__} precisa definir 'key'")

        Deduction.registry[cls.key] = cls

    @abstractmethod
    def calculate():
        pass

    def validate_amount(self, amount : float) -> float:
        if amount is None:
            return 0.0
        return max(amount, 0.0)
      