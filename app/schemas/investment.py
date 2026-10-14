from decimal import Decimal
from operator import ge, gt, le
from typing import Literal

from pydantic import BaseModel, Field, ConfigDict


class InvestmentScenarioRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    initial_amount: Decimal = Field(
        gt=0,
        max_digits=12,
        decimal_places=2,
    )

    annual_rate: Decimal = Field(
        ge=0,
        le=10,
        max_digits=12,
        decimal_places=10,
    )
    years: int = Field(gt=0, le=100)

class ScenarioResult(BaseModel):
    annual_rate: Decimal
    final_amount: Decimal
    gross_profit: Decimal


class InvestmentComparisonRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    scenario_a: InvestmentScenarioRequest
    scenario_b: InvestmentScenarioRequest


class InvestmentComparisonResponse(BaseModel):
    initial_amount: Decimal
    years: int
    scenario_a: ScenarioResult
    scenario_b: ScenarioResult
    absolute_difference: Decimal
    higher_amount: Literal["A", "B", "equal"]
    limitations: list[str]
