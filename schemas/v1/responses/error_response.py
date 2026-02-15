from pydantic import BaseModel

class ErrorResponse(BaseModel):
    code: int
    message: str
    details: str | None = None
