import json

with open("countries.json", "r", encoding="utf-8") as file:
    country: list[dict[str:str]] = json.load(file)

    data_total: dict[str : list[str]] = {}

    for data in country:
        data_total.setdefault(data['religion'], []).append(data['country'])

with open("religion.json", 'w', encoding='utf-8') as file:
    json.dump(data_total, file)