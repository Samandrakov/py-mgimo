import json
import pathlib

import pandas as pd
from countries_ru import capital_cities_by_country

df = pd.read_csv("countries_en.csv")[["Country", "Capital"]]
df.to_csv("capital_cities_en.csv", index=False)

content = json.dumps(capital_cities_by_country, indent=2, ensure_ascii=False)
path = pathlib.Path(__file__).parent / "capital_cities_ru.json"
path.write_text(content, encoding="utf-8")
