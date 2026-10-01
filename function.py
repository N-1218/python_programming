import numpy as np
arr= np.zeros(3,dtype=int)
print(arr) 
print(arr.dtype)


import numpy as np
arr= np.ones(3,dtype=int)
print(arr)
print(arr.dtype)

import numpy as np
arr=np.eye(3,4)
print(arr)


import numpy as np
arr=np.diag([1,2,3])
print(arr.ndim)


import numpy as np
arr=np.random.randint(1,10,10)
print(arr)