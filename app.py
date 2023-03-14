import pandas as pd
import numpy as np

# # Read CSV -> DataFrame
# ducks = pd.read_csv("ducky.csv")
# print(ducks)
# print(ducks.dtypes)

# # Spreadsheet (requires openpyxl)
# ducks.to_excel("ducky.xlsx", sheet_name="chickens", index=False)

# # Read XLSX -> DataFrame
# chickens = pd.read_excel("ducky.xlsx")
# print(chickens)

import matplotlib.pyplot as plt

plt.close("all")
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()