import pandas as pd
import json

FILE_NAME = 'train.json'

with open(FILE_NAME, 'r') as statfile:
    data = statfile.read()

obj = json.loads(data)
columns = [x for x in obj['metric_names']]
df = pd.DataFrame(obj['stats'], columns=columns)

CSV_NAME = 'train.csv'
df.to_csv(CSV_NAME)
