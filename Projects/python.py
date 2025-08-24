import matplotlib.pyplot as plt
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



import numpy as np 
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
# print(a)
# print(np.zeros(a))
# print()
# print(np.ones(a))
# print(np.eye(4))
# print(a.ndim)
# print(np.add(a,b))
# print(a+b)
# print(np.mean(a))
twoD=np.array([[1,2,3,4],[5,6,7,8]])
print(twoD.reshape(2,4))
print(f'minimum = {np.mean(a)}\n maximum = {np.max(a)}\n')
print(twoD.T)