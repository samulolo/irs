from fastapi import FastAPI
from routes.v1.irs_calculator_route import irs_route
from fastapi.middleware.cors import CORSMiddleware
from exceptions.global_exceptions import regist_exceptions
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"]
)

routes = [irs_route]

for route in routes:
    app.include_router(route)

regist_exceptions(app)


import json

file_name = "irs_data_2025.json"

BASE_DIR = Path("core") / f"irs_data_2025.json"

print("DIRTÓRIO DO PROEJTO: ",BASE_DIR)


with open("core/irs_data_2025.json", 'r', encoding="UTF-8") as f:
    data = json.load(f)
    print(data)