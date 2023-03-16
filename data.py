import numpy as np
import pandas as pd

"""
SERIES
1-D Data Structure
pd.Series()

Params:
Created by passing a list of values, refered to in the series 
by a default integer index

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
			"Mykolyk, Topher",
			"Hsia, Talia",
			"Park, Gitae",
      "Yuen, Jasmine"
		],
		"Age": [2,90,17,17,18]
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

# # Data Types
# print(df.dtypes)
# print("\n")

# # Heads and Tails
# print(df.head(1))
# print(df.tail(1))
# print("\n")

# # Index and Columns
# print(df2.index)
# print(df2.columns)
# print("\n")

"""
OPERATIONS on DataFrames or Series
Exclude missing data

To copy, df.copy()

Stats
df.mean() or df.mean(1) on respective axis
df.sum
s.shift(<num>)
df.apply(lambda x: <val>) appies a user defined function to the data
s.value_counts() counts values in histogram style

String methods
s.str.lower() makes all strings lowercase

pd.concat(<array of pieces>) to concatenate pandas objects
pd.merge(<obj1>, <obj2>, on=<key>) to SQL style join types along specific columns

Grouping methods
df.groupby(<label>) or df.groupby(<ordered array of labels>)
df.stack() and df.unstack()

category (a dtype)
df[<label>].astype("category")

"""

# # max()
# print(s.max())
# print(df["Age"].max())
# print("\n")

# # describe()
# print(df.describe())
# print("\n")

# # to_numpy() --- index and column labels trashed
# """ Note that this can be an expensive operation when your DataFrame has columns with 
# different data types, which comes down to a fundamental difference between pandas 
# and NumPy: NumPy arrays have one dtype for the entire array, while pandas DataFrames 
# have one dtype per column. Function may end up having to cast every value to a Python 
# object. """
# array = df.to_numpy()
# print(array)

# # T() -- transpose
# print(df.T)
# print("\n")

# # sort_index(axis=<axis>) 
# print(df.sort_index(axis=0, ascending=False))
# print("\n")

# # sort_values(by=<label>)
# print(df.sort_values(by="Name"))
# print("\n")

"""
SELECTION

df["Name"] is the same as df.Name, yielding a Series
df[index1:index2] slices the rows (inclusive index1, exclusive index2)
df.loc[<index>] or df.at[<index>, <label>] gets a cross section using a label
df.iloc[<index1>, <index2>] or df.iloc[<indexRange1>, <indexRange2>] selects by position
"""

# Boolean Indexing
print(df[df["Age"] < 18])
print("\n")

# Note: All values must be be able to pass through the boolean
# NaN where values do not satisfy the boolean condition
print(df2[df2 > 0])
print("\n")

# isin() - Value is in the row
print(df[df["Age"].isin([16, 18])])

"""
SETTING VALUES

By label, df2.at[<index>, <label2>] = <value>
By position, df2.iat[<index1>, <index2>] = <value>
To a numPy array, df.loc[<label> :, <label>] = <np.array>

"""

# at()
# df.at[1, "Age"] = 20
# print(df)

"""
MISSING DATA

df.dropna() drops rows with missing data
df.fillna(value=<value>) fills missing data
isna() gets the boolean mask where values are nan

"""