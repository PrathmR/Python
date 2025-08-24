import numpy as np

#1D ARRAY

"""
arr_1d=np.array([1,2,3,4])
print(arr_1d)
print(type(arr_1d))
print(arr_1d.ndim)"""

#2D ARRAY and few numpy functions

"""arr2d = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2d)
print(arr2d.ndim)
print(arr2d.shape)
print(arr2d.dtype)
print(arr2d.size)"""

#apending alements to an array using list

"""l=[]
for i in range(1,5):
    int_1 = int(input("Enter element to insert : "))
    l.append(int_1)
    array = np.array(l)
    print(array)"""

#creating array by defining dimensions before

"""arr = np.array([1,2,3,4], ndmin=10)
print(arr)
print(arr.ndim)"""

#create Numpy array using Numpy functions 
"""ar_zero=np.zeros((4,3))
print(ar_zero)#fill zero
ar_one=np.ones((4,3))
print(ar_one)#fill one
ar_empty=np.empty(4)
print(ar_empty)#empty array(stores the previous memory and assigns to empty values correspondingly
ar_r=np.arange(4)
print(ar_r)#creates an array of range till 4
ar_d=np.eye(3)
print(ar_d)#create an array of dimension 3 with diagonoal elements as 1
ar_li=np.linspace(0,20,num=5)
print(ar_li)#creates an array from elements 0 to 20 with space of 5(i.e., prints each 5th element of the total elements )"""

#create Numpy arrays with random number
"""var1=np.random.rand(3,4)
print(var1)#creates an array of 3*4 with random values ranges from 0 to 1
var2=np.random.randn(5)
print(var2)#generates random numbers close to zero (may be +ve or -ve)
var3=np.random.ranf(4)
print(var3)#generates random numbers in float from [0.0, 1.0)
var4=np.random.randint(0,20,5)
print(var4)#creates an array with 5 random numbers from 0 to 20 """

#changing data type of data
"""arr = np.array([1,2,3],dtype =np.float32)
print(arr)

#using datatype as a fucntion
x= np.array([1,2,3])
new = np.float32(x)
print(x,x.dtype, new.dtype)

#using astype
y= np.array([1,2,3,4])
new1=y.astype(float)
print(y, y.dtype, new1.dtype)"""

#Arithematic operations in an array
"""varA= np.array([1,2,3,4])
varB =np.array([5,6,7,8])
add=np.add(varA,varB)
mul=np.multiply(varA,varB)
div= np.divide(varA,varB)
mod= np.mod(varA,varB)
power=np.power(varA,varB)
print(add,mul,div,mod,power)"""


#Arithematic functions in Numpy array(minimum ,max, argmin,argmax, sqrt,cumsum
"""A= np.array([2,56,87,4,7])
print(np.min(A),np.max(A),np.argmin(A),np.argmax(A),np.sqrt(A),np.cumsum(A))"""

#finding min/ma xof an 2D array

"""A2D= np.array([[1,2,3],[4,5,6]])
print(np.min(A2D, axis=1)) #finding elements through row
print(np.min(A2D, axis=0))#finfing elements throw col"""

#Reshaping size of an 1D to 2Darray
"""arr_reshape= np.array([2,5,6,8,9,10])
rp=arr_reshape.reshape(3,2)#product of this must be equal to number of elements in array else error
print(rp)"""

#Reshaping 2D array to 1D
"""A1D= np.array([2,3,4,5,7,3,4,5,5])
print(A1D.reshape(-1))"""



