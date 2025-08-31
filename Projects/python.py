# import matplotlib.pyplot as plt
# x=['A','B','C']
# y=[6,7,8]
# plt.bar(x, y,color='red')
# plt.show()


# data=[10,10,20,3,3,4,15,60,70]
# plt.hist(data)
# plt.xlabel()
# plt.show()


# import numpy as np

# x = np.arange(14)
# y = np.sin(x / 2)

# plt.step(x, y + 2, label='pre (default)')
# plt.plot(x, y + 2, 'o--', color='grey', alpha=0.3)

# plt.step(x, y + 1, where='mid', label='mid')
# plt.plot(x, y + 1, 'o--', color='grey', alpha=0.3)

# plt.step(x, y, where='post', label='post')
# plt.plot(x, y, 'o--', color='grey', alpha=0.3)

# plt.grid(axis='x', color='0.95')
# plt.legend(title='Parameter where:')
# plt.title('plt.step(where=...)')
# plt.show()
# import pandas as pd
# data=pd.Series([80,90,100],index = ['pranab','chirag','harsha'])
# data_df=pd.DataFrame(data,columns=["data"])
# print(data_df)



# import numpy as np 
# a=np.array([1,2,3,4])
# b=np.array([5,6,7,8])
# print(a)
# print(np.zeros(a))
# print()
# print(np.ones(a))
# print(np.eye(4))
# print(a.ndim)
# print(np.add(a,b))
# print(a+b)
# print(np.mean(a))
# twoD=np.array([[1,2,3,4],[5,6,7,8]])
# print(twoD.reshape(2,4))
# print(f'minimum = {np.mean(a)}\n maximum = {np.max(a)}\n')
# print(twoD.T)

# import pandas as pd
# s=pd.Series([20,33,44,55], index=['A', 'B', 'C','D'])
# print(s.head())
# print(s.tail())
# print(s.describe())

# Data={'names':['veer','sahana','shreya'],'age':[20,30,40]}
# df=pd.dataframe(Data)
# print(df)
#df = pd.read_csv('C:\Users\Lenovo\OneDrive\NAGU\Documents\Python\Projects\SuperStore-sales\data\superstore.csv')

#Creating a CSV File
# %%writefile foo.csv
# date,col1,col2,col3
# 2023-01-01,a,b,1
# 2023-01-02,a,b,2
# 2023-01-03,c,d,3

# df=pd.read_csv('foo.csv',index_col=0,parse_dates=True),
# print(df)



# import numpy as np
# import matplotlib.pyplot as plt
# x=np.array([1,2,3,4,5])
# y=np.array([5,6,7,8,9])
# plt.plot(x,y)
# plt.show()
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('X vs Y')
# plt.bar(x,y,color='red')
# plt.title('Bar Graph')
# plt.show()
# plt.hist(y)
# plt.title('Histogram')
# plt.show()
# plt.scatter(x,y)  
# plt.title('Scatter Plot') 
# plt.show()
# plt.pie(y,labels=x) 
# plt.title('Pie Chart')
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# print(sns.__version__)
# df=sns.load_dataset('iris')
# print(df.head())
# sns.scatterplot(data=df,x='sepal_length',y='sepal_width',hue='species')
# plt.show()
# sns.boxplot(data=df,x='species',y='sepal_length')
# plt.show()
# sns.violinplot(data=df,x='species',y='sepal_length')
# plt.show()

import sklearn as sk
print(sk.__version__)