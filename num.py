# numpy for heavy mathematics

import numpy as np

# ls=[1,2,3,4,5]
# arr=np.array(ls)
# print(arr)
# print(len(arr))

# for n in arr:
#     print(n)

arr=np.arange(0,5,1)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)

sm=np.sum(arr)
print(np.max(arr))
print(np.mean(arr))
print(np.std(arr))

for i in arr:
    print(i)