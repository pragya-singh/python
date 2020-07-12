import numpy as np

def nn(x, W0, L):
	h = x

	for l in range(0, L-1):
		h = np.dot(W0[l],h)

	h = np.dot(W0[L-1],h)
	return h

if __name__ == '__main__':

	W0 = [np.array([[1,1,0,0],
				   [0,0,1,1]]),
		  np.array([[1,0],
		           [0,1]]),
		  np.array([[1,0],
		  			[0,1]])]

	vec_x = np.array([0,0,0,0])
	print(vec_x)
	print(nn(vec_x, W0, len(W0)))
	
	vec_x = np.array([1,0,0,1])
	print(vec_x)
	print(nn(vec_x, W0, len(W0)))

	vec_x = np.array([1,1,1,1])
	print(vec_x)
	print(nn(vec_x, W0, len(W0)))