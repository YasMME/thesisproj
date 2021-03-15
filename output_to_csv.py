import pandas as pd
import json
import sys


INPUT_FILE_NAME = sys.argv[0]
OUTPUT_FILE_NAME = sys.argv[1]

with open(INPUT_FILE_NAME, 'r') as statfile:
    data = statfile.read()

obj = json.loads(data)
columns = [x for x in obj['metric_names']]
df = pd.DataFrame(obj['stats'], columns=columns)

df.to_csv(OUTPUT_FILE_NAME)
