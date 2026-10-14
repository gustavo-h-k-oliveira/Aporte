from app.services import analysis
from fastapi import APIRouter, HTTPException

from app.domain.investment import InvestmentScenario
from app.schemas.investment import (
    InvestmentComparisonRequest,
    InvestmentComparisonResponse,
)
from app.services.analysis import InvestmentAnalysisService


router = APIRouter()
analysis_service = InvestmentAnalysisService()


@router.post(
    "/investments/compare",
    response_model=InvestmentComparisonResponse,
)
def compare_investments(
    request: InvestmentComparisonRequest,
) -> InvestmentComparisonResponse:
    try:
        scenario_a = InvestmentScenario(
            initial_amount=request.scenario_a.initial_amount,
            annual_rate=request.scenario_a.annual_rate,
            years=request.scenario_a.years,
        )

        scenario_b = InvestmentScenario(
            initial_amount=request.scenario_b.initial_amount,
            annual_rate=request.scenario_b.annual_rate,
            years=request.scenario_b.years,
        )

        result = analysis_service.analyze(scenario_a, scenario_b)

        return InvestmentComparisonResponse(**result)

    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        ) from error
