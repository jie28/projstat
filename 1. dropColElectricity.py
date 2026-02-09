import pandas as pd

df = pd.read_csv('./elecgen.csv')

columns = ['Area', 'ISO 3 code', 'Year','Continent','EU','OECD','G20','G7','ASEAN','Category','Subcategory','Variable','Unit','Value','YoY absolute change','YoY % change']
dupl_area = ['EU', 'OECD', 'G20', 'G7', 'ASEAN', 'World', 'Europe', 'Asia', 'Latin America and Caribbean', 'Middle East', 'North America', 'Oceania', 'Africa']

df = df[columns]
df.drop(df.loc[df['Area'].isin(dupl_area)].index, inplace=True)
df.drop(df[df['Year'] == 2025].index, inplace=True)
df.drop(df[df['Category'] == 'Electricity demand'].index, inplace=True)

df.to_csv('./elecgen2.csv', index=False)