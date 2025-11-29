import numpy as np
import pandas as pd

print(np.zeros((5,3)) +7)

print(np.linspace(9, 15, 20))
#array([ 9.        ,  9.31578947,  9.63157895,  9.94736842, 10.26315789,
 ##      10.57894737, 10.89473684, 11.21052632, 11.52631579, 11.84210526,
   #    12.15789474, 12.47368421, 12.78947368, 13.10526316, 13.42105263,
    #   13.73684211, 14.05263158, 14.36842105, 14.68421053, 15.        ])
print("\n", np.ones(10) * 5, "\n")
# array([5., 5., 5., 5., 5., 5., 5., 5., 5., 5.])
ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'],  )
print("\n", ser1, "\n")

df = pd.DataFrame( np.random.rand(4,4), [ '00', '11', '12', '13' ],  [ 'A', 'B', 'C', 'D' ])
print("\n", df, "\n")

print(" Column  B", df['B'], "\n")

a = np.array([1, 3, 5, 2 ,7 , 5])#
print(a)

from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'],  ['W', 'X', 'Y', 'Z']   )
print("DataFrame \n", df, "\n")



print(df['Y'])
print(df.loc['B'])
print(df.iloc[3] )
print(df[df > 0])

data = pd.read_csv('001 Lending-company.csv', index_col = 'LoanID')
lending_co_data = data.copy()
lending_co_data.head()
lending_co_data['TotalPrice'].sum()
print(lending_co_data.head())

lending_co_data.info()

lending_co_data.columns
lending_co_data['Product']
lending_co_data.shape
(1043, 14)
# open Salaries.csv as sal
# create a copy in memory
#  read out the head


sal = pd.read_csv('Salaries.csv')
salariesdata = sal.copy()
print(salariesdata.head())



# What is salaries info
print(salariesdata.info())


# What is the average BasePay
print(salariesdata['BasePay'].mean())

# What is the highest amount of vertimePay in the dataset
print(salariesdata['OvertimePay'].max())
# What is the job title of JOSEPH DRISCOLL?  Note:  Use all caps, as there is also a Joseph Driscoll
print(salariesdata[salariesdata['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'] )
# How much does JOSEPH DRISCOLL make (including benefits) ?
print(salariesdata.head())
print(salariesdata[salariesdata['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'] )

# What is the name of the highest paid persn ( including benefit) ?
print(salariesdata[salariesdata['TotalPayBenefits'] == salariesdata['TotalPayBenefits'].max()]['EmployeeName'] )
#  What is the name of the lowet paid person ( including benefits ) ?
print( salariesdata[salariesdata['TotalPayBenefits'] == salariesdata['TotalPayBenefits'].min()]['EmployeeName']       )
