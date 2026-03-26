import pandas as pd
# Create a DataFrame
data = {"name":["alice","bob","jacky"],"age":[23,24,25]}
df = pd.DataFrame(data)
 
print(df)    # Filtering rows based on a condition
print(df["name"]) # Filtering rows based on a condition
print(df[df["age"] > 30]) # Filtering rows based on a condition