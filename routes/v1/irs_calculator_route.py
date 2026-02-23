from fastapi import APIRouter, Depends, status
from schemas.v1.requests.IRSCalculationRequest import IRSCalculationRequestSchema
from services.irs_calculation_service import IrsCalculationService
from fastapi.responses import JSONResponse
from schemas.v1.responses.irs_calculation_response import IRSCalculationResponseSchema
from routes.v1.dependecies import get_irs_calculator_service
from schemas.v1.responses.error_response import ErrorResponse
from routes.v1.dependecies import get_irs_loader
from schemas.v1.loader.irs_context import IRSContext


irs_route = APIRouter(prefix="/api/irs", tags=["irs"])

responses = {
    400: {"model": ErrorResponse, "description": "Dados inválidos"},
    422: {"model": ErrorResponse, "description": "Erro de validação"},
    500: {"model": ErrorResponse, "description": "Erro interno"}
}

@irs_route.post("/{year}/v1/calculate", response_model=IRSCalculationResponseSchema,
                status_code=status.HTTP_200_OK, responses=responses)
def calculate(year: int ,request : IRSCalculationRequestSchema,
               irs_calculator_service : IrsCalculationService = Depends(get_irs_calculator_service),
               context : IRSContext = Depends(get_irs_loader)):
    
    response = irs_calculator_service.calculate(request, context).model_dump()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response)

