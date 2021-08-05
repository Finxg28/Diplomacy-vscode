import pandas as pd
path = "C:\\Users\\finch\\Documents\\roke work exprience\\"
file = 'first-json-from-data-set.json'
df = pd.read_json(path + file)
print(df)