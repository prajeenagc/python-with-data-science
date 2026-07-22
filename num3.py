import numpy as np

arr=np.array([10,20,30,40,50,60])

# print(arr)
# print(arr[0])
# print(arr[1:4])

arr2=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

# print(arr2[0,0])

# print(arr[::2])
# print(arr[::-1])

# print(arr2[:1,::])

# ar=arr.reshape(3,2)
# print(arr2.shape)
# ar1=arr.reshape(1,3,2)
# print(ar1)


arr5=np.arange(12)
print(arr5)
print(arr5.reshape(6,2))
print(arr5.reshape(2,6))
print(arr5.reshape(3,4))
print(arr5.reshape(4,3))

