from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from exceptions.greater_than_zero_exception import GreaterThanZeroException
from exceptions.irs_business_rule_exception import IRSBusinessRuleException
from schemas.v1.responses.error_response import ErrorResponse

def regist_exceptions(app: FastAPI):

    @app.exception_handler(GreaterThanZeroException)
    def handler_greater_than_zero(request: Request , exc : GreaterThanZeroException):
        return JSONResponse(
            content=ErrorResponse(code=status.HTTP_400_BAD_REQUEST, message=exc.__str__()).model_dump(),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    @app.exception_handler(IRSBusinessRuleException)
    def handle_irs_business(request: Request, exc : IRSBusinessRuleException):
        return JSONResponse()