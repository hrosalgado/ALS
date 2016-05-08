__author__ = 'Julián'

import os
import json

def toJson(dict, file):
    with open(file, "wt") as f:
        json.dump(dict, f)

def toDict(file):
    with open(file, "rU") as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    dictTemp = {"Madrid": 25, "Ourense": 35, "Vigo": 15}
    file = "temps.json"

    toJson(dictTemp, file)
    print(toDict(file))