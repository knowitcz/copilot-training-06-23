import pytest
from app.validator.amount_validator import AmountValidator, PositiveAmountValidator

def test_amount_validator_raises_on_too_large():
    validator = AmountValidator()
    with pytest.raises(ValueError, match="exceed 10000"):
        validator(20000)

def test_amount_validator_ok():
    validator = AmountValidator()
    # Should not raise
    validator(5000)

def test_positive_amount_validator_raises_on_zero():
    validator = PositiveAmountValidator()
    with pytest.raises(ValueError, match="greater than 0"):
        validator(0)

def test_positive_amount_validator_raises_on_negative():
    validator = PositiveAmountValidator()
    with pytest.raises(ValueError, match="greater than 0"):
        validator(-5)

def test_positive_amount_validator_ok():
    validator = PositiveAmountValidator()
    # Should not raise
    validator(10)
