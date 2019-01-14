import numpy as np

class Network(object):
	def __init__(self, sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
		self.weighs = [np.random.randn(y, x)
						for x, y in zip(sizes[:-1], sizes[1:])]
	
	def sigmoid(z):
		return 1.0/(1.0+np.exp(-z))
	
	def feedforward(self, a):
		"""return the output of network if "a" is input."""
		for b, w in zip(self.biases, self.weighs):
			a = sigmoid(np.dot(w, a)+b)
		return a

	def SGD(self, training_data, epochs, mini_batch_size, eta,
			test_data=None):
		"""Train the neural network using mini-batch stochastic
        gradient descent.  The "training_data" is a list of tuples
        "(x, y)" representing the training inputs and the desired
        outputs.  http://tensorfly.cn/home The other non-optional parameters are
        self-explanatory.  If "test_data" is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
		if test_data: n_test = len(test_data)
		n = len(training_data)
		for j in xrange(epochs):
			random.shuffle(training_data)
			mini_batches = [
				training_data[k:K+mini_batch_size]
				for k in xrange(0, n, mini_batch_size)]
			for  



