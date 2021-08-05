import pandas as pd
data = {
    "Name": ["Jim", "Dwight", "Angela", "Tobi"],
    "Age": [26, 28, 27, 32],
    "Department": ["Sales", "Sales", "Accounting", "Human Resources"]
}

# dataframe from dict
df = pd.DataFrame.from_dict(data)

# print the dataframe
print(df)
print(df)