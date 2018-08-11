```
This python file is a goood starting point.
Activation Functions
```

#libraries
import numpy as np

def sigmoid(x):
  # enter code below
  return (1 / (1 + np.exp(-x)))

def tanh(x):
  # enter code below
  return (np.tanh(x))
  
def relu(x):
  # entr code below
  return np.max(0,x)
  
