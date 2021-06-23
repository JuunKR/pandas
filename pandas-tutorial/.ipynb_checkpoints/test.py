import pandas as pd








df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
print(df)
print('*'*100)
print(type(df))
print('*'*100)
print(df['A'])
print('*'*100)
print(type(df['A']))
print('*'*100)
print(df.loc[df['A']])
print('*'*100)
print(type(df.loc[df['A']]))
print('*'*100)