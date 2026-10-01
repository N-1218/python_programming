import numpy as np
try:
 a=np.array([10,20,30,40])
#           +   +  +  +
 b=np.array([50,60,70,9])
 result=a+b
 print(result)
except:
 print("not allowed")
finally:  
 print("run")

#op-----[60 80 100 120 ]