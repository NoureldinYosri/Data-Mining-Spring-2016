import numpy as np;
from scipy.stats import norm

class NB:
	mu = None;
	P = None;	
	sd = None;
	n = None;
	
	def __init__(self,n):
		self.mu = [[] for i in xrange(n)];
		self.P = [0 for i in xrange(n)];
		self.n = n;

	def train(self,X,Y):	
		m = len(X);
		d = len(X[0]);	
		self.sd = np.array([np.array([0.0 for j in xrange(d)]) for i in xrange(self.n)]);
		for i in xrange(self.n):
			Z = [];
			for j in xrange(m):
				if Y[j] == i: 
					Z.append(X[j]);
			ni = len(Z);
			self.P[i] = ni*1.0/m;
			if ni == 0: self.P[i] = 1e-15;
			if ni: self.mu[i] = np.true_divide(np.sum(Z,0),ni);
			else : self.mu[i] = np.array([0 for j in xrange(d)]);	
			Z = [z - self.mu[i] for z in Z];
			for j in xrange(d):
				for z in Z:
					self.sd[i][j] += z[j]**2;
				self.sd[i][j] = np.true_divide(self.sd[i][j],ni - 1);
				self.sd[i][j] = np.sqrt(self.sd[i][j]);
				self.sd[i][j] = max(self.sd[i][j],1e-15);
					
	def predict_one(self,X):
		d = len(X);
		post = [0 for i in xrange(self.n)];
		for i in xrange(self.n):
			post[i] = self.P[i];
			for j in xrange(d):
				post[i] *= norm.pdf(X[j],loc = self.mu[i][j],scale = self.sd[i][j]);
		#print post,;
		return np.argmax(post);
	def predict(self,X):
		return [self.predict_one(x) for x in X];
	
	def accuracy(self,Y,y):
		return sum([Y[i] == y[i] for i in xrange(len(Y))])*100.0/len(Y);
	
	def recall(self,Y,y):
		ret = [[0.0, 0.0 ,0.0 ,0.0] for i in xrange(self.n)]
		for i in xrange(self.n):
			for j in xrange(len(Y)):
				if Y[j] == i and y[j] == i: ret[i][3] += 1;   #true positive
				elif Y[j] == i : ret[i][2] += 1;              #false negative
				elif y[j] == i : ret[i][1] += 1;              #false positive
				else : ret[i][0] += 1; 			      #true negative;
			for j in xrange(4) : ret[i][j] *= 100.0/len(Y);
	
		return ret;
#t = NB(2);
#X = np.array([[1 ,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16]])
#Y = np.array([0,1,0,1,0,1,0,1])
#t.train(X,Y);
#print t.sd
#print t.mu;
#print t.P
#print 
#for i in xrange(5):
#	print X[i],Y[i],t.predict_one(X[i])
