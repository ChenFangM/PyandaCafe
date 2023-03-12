import numpy as np
import pandas as pd

"""
SERIES
1-D Data Structure
pd.Series()

Params:
Created by passing a list of values, refered to in the series by a default integer index

Optional - Change data type: dtype="<dtype>"
Optional - Change name: name="<name>"

"""

s = pd.Series([3,1,4,1,5], dtype="int32")

print(s)
print("\n")


"""
DATAFRAMES
2-D Data Structure (Each column is a Series) --- Visualize as a table
pd.DataFrame(inputs)

Inputs:
Created by passing a dictionary of objects
OR...
Created by passing a NumPy array, index, and column label

Optional - Change default index: index=<indexRange>
Optional - Change column labels: column=<listOfLabels>

"""

df = pd.DataFrame(
	{
		"Name": [
			"Tieu, Brianna",
			"Kwok, Jeremy",
			"Li, Mark",
			"Kang, Brian",
		],
		"Age": [17,17,18,17]
	}
)

print(df)
print("\n")

df2 = pd.DataFrame(
	np.random.randn(5,4),
	index = pd.date_range("20050402", periods = 5),
	columns = list("FANG")
)

print(df2)
print("\n")

# Data Types
print(df2.dtypes)
print("\n")

# Heads and Tails
print(df2.head(1))
print(df2.tail(1))
print("\n")

"""
Operations on DataFrames or Series

"""

# max()
print(s.max())
print(df["Age"].max())

# describe()
print(df.describe())
