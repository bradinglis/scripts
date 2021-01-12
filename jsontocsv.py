import pandas as pd
path = r'C:\Users\InglisB\Documents\CRMDataStuff\working\rail_completed_jobs'
df = pd.read_json (path + r'.json')
df.T.to_csv (path + r'.csv', index = None, header=True)