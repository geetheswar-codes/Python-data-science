# pandas dataframe basics
import pandas as pd
# creating a dataframe
data = {
  "Name":["Alice","Bob","Charlie","Davide"],
  "Age":[23, 25, 22, 24],
  "Marks":[85, 90, 78, 88]
}
df= pd.DataFrame(data)
print("DataFrame:",df)

print("\nshape of DataFrame:",df.shape)
print("\nColumn name:",df.columns)
print("\nData types:",df.dtypes)
