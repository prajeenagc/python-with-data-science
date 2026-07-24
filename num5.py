import numpy as np
arr=np.array([10,np.nan,20,np.nan,40,50])

# print(arr.size)
# print(arr.ndim)
# print(arr)
# print(np.isnan(arr))

clean_data=arr[~np.isnan(arr)]
# print(clean_data)

# mean=np.nanmean(arr)
# arr[np.isnan(arr)]=mean
# # print(arr)

# median=np.nanmedian(arr)
# arr[np.isnan(arr)]=median
# print(arr)
sums=np.nansum(arr)
arr[np.isnan(arr)]=sums
# print(arr)

arr1=([
    [1,np.nan,5],
    [3,4,np.nan]
])
arr_filled=np.nan_to_num(arr1,nan=1)
# print(arr_filled)
arr2=np.array([10,20,np.nan,30,np.nan])
arr_filled=np.nan_to_num(arr2,nan=1)
# print(np.prod(arr_filled))

sales=np.array([1000,2000,1500,3000])
growth_factor=np.array([1.1,np.nan,0.95,np.nan])
arr_filled=np.nan_to_num(growth_factor,nan=1)
# print(arr_filled)
total=sales*arr_filled
# print(total)
data=[10,85,88,90,92,95]
ages=np.array([20,25,np.nan,30,35],dtype=float)
mean_age=np.nanmean(ages)
print(mean_age)

#we replace nan value 


income=[30000,35000,40000,5000000,np.nan]
income=np.array(income,dtype=float)
print("Original income:", income)
median_income=np.nanmedian(income)
income[np.isnan(income)]=median_income
print(median_income)

