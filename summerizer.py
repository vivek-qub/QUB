import pandas as pd

df = pd.read_excel('C:\\Users\\vivek\\qubryx\\python\\data.xlsx')

print(f"Number of rows: {len(df)}")
print(f"Number of columns: {len(df.columns)}")
