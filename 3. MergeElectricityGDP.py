import pandas as pd

gdp = pd.read_csv('./gdpnew.csv')

elec = pd.read_csv('./elecgen2.csv')

cl = ['Area', 'ISO 3 code', 'Year', 'Continent', 'EU', 'OECD', 'G20', 'G7', 'ASEAN', 'Category', 'Subcategory', 'Variable', 'Unit', 'Value', 'YoY absolute change', 'YoY % change']

df = pd.DataFrame()
cc = [x for x in elec['ISO 3 code'].unique()]

for i in gdp['Country Code']:
    if i in cc:
        for j in range(2000, 2025):
            print(i, j)
            data = {
                'Area': elec.loc[elec['ISO 3 code'] == i, 'Area'].unique()[0],
                'ISO 3 code': i,
                'Year': j,
                'Continent': elec.loc[elec['ISO 3 code'] == i, 'Continent'].unique()[0],
                'EU': int(elec.loc[elec['ISO 3 code'] == i, 'EU'].unique()[0]),
                'OECD': int(elec.loc[elec['ISO 3 code'] == i, 'OECD'].unique()[0]),
                'G20': int(elec.loc[elec['ISO 3 code'] == i, 'G20'].unique()[0]),
                'G7': int(elec.loc[elec['ISO 3 code'] == i, 'G7'].unique()[0]),
                'ASEAN': int(elec.loc[elec['ISO 3 code'] == i, 'ASEAN'].unique()[0]),
                'Category': 'GDP',
                'Subcategory': 'GDP',
                'Variable':  'GDP',
                'Unit': '$',
                'Value': round(gdp.loc[gdp['Country Code'] == i, str(j)].unique()[0], 2),
                'YoY absolute change': round((gdp.loc[gdp['Country Code'] == i, str(j)].unique() - gdp.loc[gdp['Country Code'] == i, str(j-1)].unique())[0], 2),
                'YoY % change': round((gdp.loc[gdp['Country Code'] == i, str(j)].unique()/gdp.loc[gdp['Country Code'] == i, str(j-1)].unique() -1)[0]*100, 2),
            }
            print(data)
            df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

gf = pd.DataFrame()

gf = pd.concat([elec, df], ignore_index=True)

gf.to_csv('./elecgdp2.csv', index=False)
