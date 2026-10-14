from decimal import Decimal

import pytest

from app.domain.investment import InvestmentScenario
from app.domain.services.compound_interest import CompoundInterestCalculator
from app.services.analysis import InvestmentAnalysisService


def test_compound_interest_for_three_years() -> None:
    scenario = InvestmentScenario(
        initial_amount=Decimal("1000.00"),
        annual_rate=Decimal("0.10"),
        years=3,
    )

    result = CompoundInterestCalculator().calculate(scenario)

    assert result == Decimal("1331.000000")


def test_rejects_zero_initial_amount() -> None:
    with pytest.raises(ValueError):
        InvestmentScenario(
            initial_amount=Decimal("0.00"),
            annual_rate=Decimal("0.10"),
            years=3,
        )


def test_rejects_negative_annual_rate() -> None:
    with pytest.raises(ValueError):
        InvestmentScenario(
            initial_amount=Decimal("1000.00"),
            annual_rate=Decimal("-0.01"),
            years=3,
        )


def test_comparison_uses_same_capital_and_term() -> None:
    scenario_a = InvestmentScenario(
        initial_amount=Decimal("1000.00"),
        annual_rate=Decimal("0.10"),
        years=3,
    )

    scenario_b = InvestmentScenario(
        initial_amount=Decimal("1000.00"),
        annual_rate=Decimal("0.12"),
        years=3,
    )

    result = InvestmentAnalysisService().analyze(
        scenario_a,
        scenario_b,
    )

    assert result["scenario_a"]["final_amount"] == Decimal("1331.00")
    assert result["scenario_b"]["final_amount"] == Decimal("1404.93")
    assert result["absolute_difference"] == Decimal("73.93")
    assert result["higher_amount"] == "B"


def test_comparison_rejects_different_initial_amounts() -> None:
    scenario_a = InvestmentScenario(
        initial_amount=Decimal("1000.00"),
        annual_rate=Decimal("0.10"),
        years=3,
    )

    scenario_b = InvestmentScenario(
        initial_amount=Decimal("2000.00"),
        annual_rate=Decimal("0.12"),
        years=3,
    )

    with pytest.raises(ValueError, match="mesmo capital inicial"):
        InvestmentAnalysisService().analyze(scenario_a, scenario_b)


def test_comparison_rejects_different_terms() -> None:
    scenario_a = InvestmentScenario(
        initial_amount=Decimal("1000.00"),
        annual_rate=Decimal("0.10"),
        years=3,
    )

    scenario_b = InvestmentScenario(
        initial_amount=Decimal("1000.00"),
        annual_rate=Decimal("0.12"),
        years=5,
    )

    with pytest.raises(ValueError, match="mesmo prazo"):
        InvestmentAnalysisService().analyze(scenario_a, scenario_b)
