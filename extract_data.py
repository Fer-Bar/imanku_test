import pandas as pd

excel_file_path ='counties.xlsx'
df = pd.read_excel(excel_file_path)

df['county'] = df['county'].str.replace(r'[\W]|_', '', regex=True)
df['population'] = df['population'].fillna(0).astype(int)

df.to_excel('clean_counties.xlsx')