import numpy as np
import pandas as pd
#creating numpy arrays:
#creation of a array with the help of predefined datatypes
'''n2= np.array([[1,2,3,4,0],[14,23,0,23,4]])
print(n2)
print(n2.ndim)
print(n2.shape)

ar2=np.array([1,2,0.9,0.10])
print(ar2.dtype)
'''
#multiplying matrices
"""a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.dot(a,b)
print(result)
"""
#write a program to add all the elements present in single dimensional array
"""a=np.array([1,2,3,4])
add=np.sum(a)
print(add)"""

#zeros, ones,arange
"""zeros=np.zeros((2,4))
ones=np.ones((2,4))
arange=np.arange(3)
print(zeros,"\n", ones , "\n", arange)
"""
"""for i in range(1,5):
    int_1 = int(input("Enter element to insert : "))
    l.append(int_1)
    array = np.array(l)
    print(array)"""

#write a program to display sum of even numbers present in given array
"""array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=0
for num in array:
    if num % 2 == 0:
        even += num
print(even)
         """

#wite a program to find mean value ,median , std deviation and sum of array elements where, array elements are 3,7,6,4,1,3,8.
"""arr=np.array([3,7,6,4,1,3,8])
mean= np.mean(arr)
median=np.median(arr)
sd=np.std(arr)
add=np.sum(arr)
print(mean,"\n",median,"\n",sd,"\n",add)
"""
#write a program to display maximum number among given 3 values, without using predefined methods.
"""a=int(input("Enter the 1st number :"))
b=int(input("Enter the 2nd number :"))
c=int(input("Enter the 3rd number :"))
if a > b and a>c:
      print("A is larger")
elif b > a and b >c:
    print("B is larger")
else:
    print("C is larger")
"""

#write a program to check the given number is even or odd without using build in functions
"""a= int(input("Enter the number to check wheather it is even or odd :"))
if a & 1 == 0 :
    print(f" {a} is a even number")
else:
    print(f" {a} is a odd number")
"""

#write a program to check the given number is amstrong or not
"""numb=int(input("Enter the number:"))
str_num=str(numb)
le=len(str_num)
print(le)
total = 0
for digit in str_num:
    total += int(digit) ** le

if total==numb:
    print("yes")
else:
("Enter the number:"))
c=0
while(n>0):
    rem=n%10
    c=c+1
    n=int(n/10)
sum=0
while(n1>0)"""

#Nummpy Array
"""array=np.array([11,22,33,44,55,66,77,88,99])
print(array[0:])
print(array[-1:])
print(array[:-1])
print(array + 5)
print(array -5)
print(array / 5)
print(array * 5)
print(array // 5)"""

#Numpy Zeros, Ones
"""zero=np.zeros((5,5))
print(zero)
print(np.ones((4,5)))
print(np.arange(1,20,2))#printing odd numbers from 1 to 20
print(np.arange(0,20,2))#printing even numbers from 2 to 20"""

#LineSpace()
"""arr=np.linspace(0,10,15)
print(arr)"""

#Random function in Numpy
"""print(np.random.randint(10,20,20))
"""
"""dict = {
    'Age': np.random.randint(19,22,20),
    'Marks_Maths':np.random.randint(40,100,20),
    'Mark_Biology':np.random.randint(80,101,20),
    'Marks_AI':np.random.randint(60,100,20),
    'Sem' : np.random.randint(1,8,20)
    }

df = pd.DataFrame(dict)
print(df)
"""

"""dict={
    'age': np.random.randint(19,22,50),
    'salary': np.random.randint(10000, 200000, 50),
    'experience': np.random.randint(1,35,50),
    }
df=pd.DataFrame(dict)
print(df)
"""

##################################################################################################################################################
#Pandas --> Series 
"""list =[1,2,3]
series=pd.Series(['abc','def','ghi'], index =list)

print(series)

ser = pd.Series(['Prathmesh','Belgaum','Emperor'], index = ['Name:', 'Place:', 'Ocuupation:'])
print(ser)
"""

#DataFrames
'''data={
    'stock_price1':[10,20,30,34,53,56,67],
    'stock_price2':[15,20,25,23,45,67,89],
    'stock_price3':[20,25,30,40,78,00,99]}
df=pd.DataFrame(data)
print(df)
'''

data=np.array([1,2,3,4,np.nan,np.nan])
#Using Numpy
"""print(np.isnan(data))
print(data[~np.isnan(data)])
print(~np.isnan(data))
print(np.nanmean(data))
print(np.nansum(data))
"""
#Using Pandas
data={
    'stock_price1':[10,20,30,34,53,56,67],
    'stock_price2':[15,20,25,23,np.nan,67,89],
    'stock_price3':[20,25,30,40,78,00,np.nan]}
df=pd.DataFrame(data)
print(df.isna())



