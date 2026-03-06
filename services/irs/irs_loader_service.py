from pathlib import Path
import json


class IRSDataLoaderService:

    def load(self, year : int) -> dict:
    
        file_name = f"irs_data_{year}.json"
        BASE_DIR = Path("./core") / file_name

        if not BASE_DIR.exists():
              raise FileNotFoundError(f"Dados de IRS para o ano {year} não foram encontrados")
        
        with open(BASE_DIR, 'r', encoding="UTF-8") as f:
            return json.load(f)
        
