from decimal import Decimal, ROUND_HALF_UP

from app.domain.investment import InvestmentScenario
from app.domain.services.compound_interest import CompoundInterestCalculator


CENT = Decimal("0.01")


def round_money(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


class InvestmentAnalysisService:
    def __init__(self) -> None:
        self.calculator = CompoundInterestCalculator()

    def analyze(
        self,
        scenario_a: InvestmentScenario,
        scenario_b: InvestmentScenario,
    ) -> dict:
        if scenario_a.initial_amount != scenario_b.initial_amount:
            raise ValueError(
                "Os cenários devem ter o mesmo capital inicial."
            )

        if scenario_a.years != scenario_b.years:
            raise ValueError(
                "Os cenários devem ter o mesmo prazo."
            )

        amount_a = round_money(self.calculator.calculate(scenario_a))
        amount_b = round_money(self.calculator.calculate(scenario_b))

        profit_a = amount_a - scenario_a.initial_amount
        profit_b = amount_b - scenario_b.initial_amount

        difference = abs(amount_a - amount_b)

        if amount_a > amount_b:
            higher_amount = "A"
        elif amount_b > amount_a:
            higher_amount = "B"
        else:
            higher_amount = "equal"

        return {
            "initial_amount": scenario_a.initial_amount,
            "years": scenario_a.years,
            "scenario_a": {
                "annual_rate": scenario_a.annual_rate,
                "final_amount": amount_a,
                "gross_profit": profit_a,
            },
            "scenario_b": {
                "annual_rate": scenario_b.annual_rate,
                "final_amount": amount_b,
                "gross_profit": profit_b,
            },
            "absolute_difference": difference,
            "higher_amount": higher_amount,
            "limitations": [
                "Não considera impostos.",
                "Não considera custos.",
                "Não considera inflação.",
                "Não considera risco ou liquidez.",
                "Pressupõe taxa efetiva anual constante.",
            ],
        }
