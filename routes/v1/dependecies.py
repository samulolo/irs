from services.irs_calculation_service import IrsCalculationService
from services.irs.irs_loader_service import IRSDataLoaderService
from datetime import datetime
from schemas.v1.loader.irs_context import IRSContext


def get_irs_calculator_service():
    return IrsCalculationService()


def get_irs_loader(year : int) -> IRSContext:
    loader = IRSDataLoaderService()
    context = IRSContext(loader.load(year))
    return context
   