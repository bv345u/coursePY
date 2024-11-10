import json
def task() -> float:
    DataFromJson = json.load(open("input.json"))
    S = sum([i["score"] * i["weight"] for i in DataFromJson])
    return round(S, 3)
print(task())