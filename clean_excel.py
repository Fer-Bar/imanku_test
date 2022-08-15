import pandas as pd

excel_file_path ='counties.xlsx'

df = pd.read_excel(excel_file_path)
# Clean excel
df['county'] = df['county'].str.replace(r'[\W]|_', '', regex=True)
df['population'] = df['population'].fillna(0).astype(int)
# Convert the excel to csv format
df.to_csv('clean_counties.csv', index = None, header=False)
