import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
})


df['name']           # bracket notation (always works)
df.name              # dot notation (only for simple names)

df[['name', 'age']]          # list of column names

df.iloc[:, 0]        # first column
df.iloc[:, 1:4]      # columns at index 1 and 2
df.iloc[:, [0, 2]]   # first and third columns

df.loc[:, 'age']               # single column by name
df.loc[:, 'name':'age']        # slice of columns (inclusive)
df.loc[:, ['name', 'salary']]  # specific columns by name


df.loc[df['age'] > 25, 'name']           # filtered rows, one column
df.loc[df['age'] > 25, ['name', 'age']]  # filtered rows, multiple columns