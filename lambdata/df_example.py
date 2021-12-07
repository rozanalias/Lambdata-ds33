import pandas as pd
# Classes represtent some entity 
# Class to represent vehicles

#Classes have variables , and functions
# when we talk about variables that are associated with objects/classes we call them 'attributes'
# when we talk about functions that are assocites with objects/classes we call them 'methods

#df attributes
# attributes have no parentheses
df = pd.DataFrame({'a': [1,2,3], 'b' : [4,5,6]})
print(df.shape)
print(df.index)
print(df.dtypes)

# dataframe methods
#methods *do* have parentheses

print(df.isnull())
