import pandas as pd

# Read CSV -> DataFrame
ducks = pd.read_csv("ducky.csv")
print(ducks)
print(ducks.dtypes)

# Spreadsheet (requires openpyxl)
ducks.to_excel("ducky.xlsx", sheet_name="chickens", index=False)

# Read XLSX -> DataFrame
chickens = pd.read_excel("ducky.xlsx")
print(chickens)
