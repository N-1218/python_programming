import numpy as np
arr= np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print("Original array : ",arr)
slicing=arr[0,0:3]
slicing[:]=0
print(slicing)
print("orginal : ",arr)