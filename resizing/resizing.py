import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,8,8,8,8,88,8])
# print("Original arrray : ",arr)
# new =np.unique(arr)
# new1=np.unique(arr).size
# print("unique arrray count",new1)
# print("Unique array: ",new)

import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Dimension is : ",arr.ndim)
print("Original Array : ",arr)
new =np.unique(arr)
print("Unique array : ",new)
new1=np.unique(arr).size
print("Size of unique element : ",new1)
resize=np.resize(arr,(1,4,5))
print("resize arrray : ",resize)
print("resizing array dimention : ",resize.ndim)
