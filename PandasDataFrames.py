
import numpy as np
import pandas as pd



print(np.zeros((5, 3)) + 7)

print(np.linspace(9, 15, 20))

print(np.ones(10) * 5)

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'], )
print(ser1)

df = pd.DataFrame(np.random.rand(4, 4), ['00', '11', '12', '13'], ['A', 'B', 'C', 'D'])
print(df)

print(df['B'])
a = np.array([1, 3, 5, 2, 7, 5])  #
print(a)

type(a)

np.random.seed(101)

print(df)
