import json

rezult=[]

def f() -> float:
    namef = "input.json"
    with open(namef) as f:
        jsonlist = json.load(f)

    for item in jsonlist:
        proizv = item["score"] * item["weight"]
        rezult.append(proizv)

    summ=sum(rezult)
    return round(summ, 3)


print(f())