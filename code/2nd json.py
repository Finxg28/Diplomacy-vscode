import json
from pathlib import Path
file = Path(__file__).parents[1]/'2nd_json_from_dataset_test'
import pandas
with open(file.name) as open_file:
    df=json.load(open_file)
    print(df)
    df2= pandas.DataFrame.from_dict(df)
    #print(df["messages"])
    #print(df["players"])
    #print(df.keys())
    #for item in df.keys(): 
        #print(df[item])
        #frompathlib iterdir
    print (df2)
        
    print ("Hello")
    import matplotlib.pyplot as plt