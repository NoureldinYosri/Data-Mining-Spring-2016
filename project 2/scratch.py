import numpy as np;

sig = np.array([[0.122 ,0.098],[0.098 ,0.142]])
mu  = np.array([[5.01],[3.42]]);
x   = np.array([[6.75], [4.25]]);

det = np.linalg.det(sig);
inv = np.linalg.inv(sig);

y = x - mu;
yt = np.transpose(y);
v = -np.dot(yt,np.dot(inv,y))/2.0;

v = 2*1e-5*np.exp(v)/np.sqrt(det)/np.sqrt(2*np.pi);


X = np.array([[1,2],[3,4]])
y = np.array([0.5,0.5]);
print X-y
