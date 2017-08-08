# 简单使用numpy库
import numpy as np
a = np.ones((4,5))
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)

b = np.random.rand(5,3)
print(b)
print(b[2])
print(b[1:3])
print(b[-5:-2:2])

#  ***************************************
#  结果
#  [[ 1.  1.  1.  1.  1.]
#   [ 1.  1.  1.  1.  1.]
#   [ 1.  1.  1.  1.  1.]
#   [ 1.  1.  1.  1.  1.]]
#  2
#  (4, 5)
#  float64
#  [[ 0.79682939  0.96859263  0.7948034 ]
#   [ 0.34808704  0.10589081  0.4483378 ]
#   [ 0.01875356  0.63986908  0.33505021]
#   [ 0.85214834  0.61396681  0.81165   ]
#   [ 0.56724328  0.20352266  0.40945604]]
#  [ 0.01875356  0.63986908  0.33505021]
#  [[ 0.34808704  0.10589081  0.4483378 ]
#   [ 0.01875356  0.63986908  0.33505021]]
#  [[ 0.79682939  0.96859263  0.7948034 ]
#   [ 0.01875356  0.63986908  0.33505021]]