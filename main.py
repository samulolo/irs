from fastapi import FastAPI
from routes.v1.irs_calculator_route import irs_route
from fastapi.middleware.cors import CORSMiddleware
from exceptions.global_exceptions import regist_exceptions


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routes = [irs_route]

for route in routes:
    app.include_router(route)

regist_exceptions(app)


