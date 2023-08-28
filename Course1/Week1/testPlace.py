import numpy as np

def sigmoid(z): 
    
    ### START CODE HERE ###
    # calculate the sigmoid of z
    if isinstance(z, str):
        return
    if hasattr(z, '__len__') :
        m, n = np.shape(z)
        print(m, n)
        z = z.flatten()
        h = [1/(1+np.exp(-num)) for num in z]
        h = np.array([h])
    else:
        h = 1/(1+np.exp(-z))
    ### END CODE HERE ###
    
    return h

tmp_X = np.append(np.ones((10, 1)), np.random.rand(10, 2) * 2000, axis=1)
theta = np.zeros((3, 1))
z = np.dot(tmp_X, theta)
h = sigmoid(z)
print(sigmoid(0))
