import numpy as np
import torch
import matplotlib.pyplot as plt
arr=np.array([1, 2, 3, 4, 5])
print("NumPyar array:", arr)
tensor = torch.from_numpy(arr)
print("PyTorch tensor:", tensor)
tensor_times3=tensor*3
print("Tensor multiplied by 3:", tensor_times3)
plt.plot(arr,label='Original NumPy Array')
plt.plot(tensor_times3.numpy(), label='Tensor multiplied by 3')
plt.title('NumPy Array vs PyTorch Tensor')
plt.legend()
plt.grid(True)
plt.show()
