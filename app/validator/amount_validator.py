from typing import Protocol

class AmountValidatorProtocol(Protocol):
    def __call__(self, amount: int) -> None:
        ...

class AmountValidator(AmountValidatorProtocol):
    def __call__(self, amount: int) -> None:
        if amount > 10000:
            raise ValueError("Amount cannot exceed 10000.")

class PositiveAmountValidator(AmountValidatorProtocol):
    def __call__(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
