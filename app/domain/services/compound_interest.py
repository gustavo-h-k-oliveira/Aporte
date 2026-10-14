from decimal import Decimal

from app.domain.investment import InvestmentScenario


class CompoundInterestCalculator:
    def calculate(self, scenario: InvestmentScenario) -> Decimal:
        capital = scenario.initial_amount
        rate = scenario.annual_rate
        years = scenario.years

        return capital * pow((Decimal("1") + rate), years)
