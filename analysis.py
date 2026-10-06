import pandas as pd

data = {"Name" : ["Asha", "Bala", "Charan"], "Score":[85,90,70]}
df = pd.DataFrame(data)
print(df)
print("Average Score:", df["Score"].mean())

print("Maximum Score:", df["Score"].max())
print("Maximum Score:, df ["Score"].min())