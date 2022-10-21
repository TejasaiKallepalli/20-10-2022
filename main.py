import numpy as np
k1 = np.random.randint(1,20,15)
print(k1)
k2=np.reshape(k1,(3,5))
print(k2)
print(k2.shape)
max_element = np.amax(k2, axis = 1)
max_element = max_element[: , None]
k3 = np.where(k2 == max_element, 0, k2)
print(k3)