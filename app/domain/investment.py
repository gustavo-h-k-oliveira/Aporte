from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class InvestmentScenario:
    initial_amount: Decimal
    annual_rate: Decimal
    years: int

    def __post_init__(self) -> None:
        if not isinstance(self.initial_amount, Decimal):
            raise TypeError("initial_amount deve ser Decimal.")

        if not isinstance(self.annual_rate, Decimal):
            raise TypeError("annual_rate deve ser Decimal.")

        if self.initial_amount <= Decimal("0"):
            raise ValueError("O capital inicial deve ser maior que zero.")

        if self.annual_rate < Decimal("0"):
            raise ValueError("A taxa anual não pode ser negativa.")

        if isinstance(self.years, bool) or not isinstance(self.years, int):
            raise TypeError("years deve ser um número inteiro.")

        if self.years <= 0:
            raise ValueError("O prazo deve ser maior que zero.")
