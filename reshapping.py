import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a)
print("A Dimension: ",a.ndim)
# x=a.reshape(2,          6)
#          row(len)    col  
# x=a.reshape(3,4) 
x=a.reshape(4,3)

print("shape : ",x.shape)
print(x)
print("X dimension : ",x.ndim)
