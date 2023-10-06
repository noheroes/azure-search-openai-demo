import pandas as pd
import json

def convert_to_json(texto, key1, key2 ="", key3 = ""):
    j = json.loads(json.dumps(texto.to_dict()))
    result = json.loads(j["0"])
    if key1:
       if key2:
          if key3:
             return result[key1][key2][key3]
       else:
          return result[key1][key2]
    else:
       return result[key1]



def convert_to_json(dfColumn, key1, key2 ="", key3 = ""):
    j = json.loads(json.dumps(dfColumn.to_dict()))
    result = json.loads(j["0"])
    if key1:
       if key2:
          if key3:
             return result[key1][key2][key3]
       else:
          return result[key1][key2]
    else:
       return result[key1]

print(f'config: {config}\n')


df = pd.read_csv("salida.csv", delimiter=";", dtype={"id": str,"nombres": str,"direccion": str,"sku": str,"dni": str,"fjson": str})

print("simplificado:\n")
j = json.loads(json.dumps(df["fjson"].to_dict()))
result = json.loads(j["0"])
config = result["root"]["files"]["config"]
print(f'config: {config}\n')

print("original:\n")
fjson = df["fjson"].to_dict()
result = json.dumps(fjson)
j = json.loads(result)
result = json.loads(j["0"])
print(f"result: {result}")
config = result["root"]["files"]["config"]
print(f'config: {config}\n')




