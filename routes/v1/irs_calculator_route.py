from fastapi import APIRouter, Depends, status
from schemas.v1.requests.IRSCalculationRequest import IRSCalculationRequestSchema
from services.irs_calculation_service import IrsCalculationService
from fastapi.responses import JSONResponse
from schemas.v1.responses.irs_calculation_response import IRSCalculationResponseSchema
from routes.v1.dependecies import get_irs_calculator_service
from schemas.v1.responses.error_response import ErrorResponse


irs_route = APIRouter(prefix="/api/irs", tags=["irs"])

responses = {
    400: {"model": ErrorResponse, "description": "Dados inválidos"},
    422: {"model": ErrorResponse, "description": "Erro de validação"},
    500: {"model": ErrorResponse, "description": "Erro interno"}
}

@irs_route.post("/api/v1", response_model=IRSCalculationResponseSchema,
                status_code=status.HTTP_200_OK, responses=responses)
def calculate(request : IRSCalculationRequestSchema,
               irs_calculator_service : IrsCalculationService = Depends(get_irs_calculator_service)):
    response = irs_calculator_service.calculate(request).model_dump()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response)

