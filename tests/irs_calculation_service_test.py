import pytest
from services.irs_calculation_service import IrsCalculationService


@pytest.fixture
def calculator():
    return IrsCalculationService()


def test_should_calculate_taxable_income_and_tax_without_deductions(calculator):
    request = {
        "gross_income": 30000,
        "deductions": {
            "dependents": {
                "total": 0,
                "dependents_upto_3": 0,
                "dependents_upto_6": 0
            },
            "health": 0,
            "education": 0,
            "family": 0
        },
        "professional_order": 0
    }

    result = calculator.calculate(year=2025, data=request)

    assert result["taxable_income"] == pytest.approx(25896, abs=0.01)
    assert result["tax"] == pytest.approx(5119.30, abs=0.01)
    assert result["deductions"]["total"] == pytest.approx(0, abs=0.01)
    assert result["net_tax"] == pytest.approx(5119.30, abs=0.01)