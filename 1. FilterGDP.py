import pandas as pd

df = pd.read_csv("./gdp.csv", index_col=[0])

ef = df.drop(df.columns[[x for x in range (3, 42)]], axis=1)
ef.drop(ef.filter(regex="Unnamed"), axis=1, inplace=True)
ef.to_csv('./gdpnew.csv')