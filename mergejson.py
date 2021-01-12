import json
from jsonmerge import merge
import pandas as pd

jsonfile1 = r'C:\Users\InglisB\Documents\CRMDataStuff\working\bluescope-truck_data_0.json'
jsonfile2 = r'C:\Users\InglisB\Documents\CRMDataStuff\working\bluescope-truck_data_1.json'
out = r'C:\Users\InglisB\Documents\CRMDataStuff\working\out.json'

f = open(jsonfile1, encoding="utf8");
file1 = json.load(f)
f = open(jsonfile2, encoding="utf8");
file2 = json.load(f)
result = merge(file1, file2)

for x in range(19):
    print(x+2)
    resultl = result
    jsonfile  = r'C:\Users\InglisB\Documents\CRMDataStuff\working\bluescope-truck_data_' + str(x+2) + '.json'
    f = open(jsonfile, encoding="utf8")
    file = json.load(f)
    result = merge(resultl, file)
    

with open(out, 'w') as outfile:
    json.dump(result, outfile)
#df = pd.read_json(result)
#df.T.to_csv (out, index = None, header=True)

