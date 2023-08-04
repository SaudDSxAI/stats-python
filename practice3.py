import pandas as pd

# Create two example DataFrames
data1 = {'X': [1, 2, 3, 4, 5],'Y': [2, 4, 6, 8, 10]}
df1 = pd.DataFrame(data1)

data2 = {'A': [3, 4, 5, 6, 7],'B': [1, 3, 5, 7, 9]}
df2 = pd.DataFrame(data2)

# Calculate the covariance between the two DataFrames
covariance1 = df1['X'].cov(df2['A'])
covariance2 = df1['Y'].cov(df2['B'])
print("Covariance row1 and row2:\n", covariance1, " ", covariance2)
