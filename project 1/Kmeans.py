import numpy as np
import csv;

def dist2(X,Y):
	X = X - Y
	return sum(X*X);

def get_initial(X,k):
	from random import randint;
	n = len(X);
	C = set();
	while len(C) < k:
		i = randint(0,n - 1);
		if i not in C: C.add(i);
	return [X[c] for c in C];

def create_clusters(X,C,n,k):
	clusters = [[] for i in xrange(k)];
	for i in xrange(n):
		DIST = [dist2(X[i],c) for c in C];
		clusters[np.argmin(DIST)].append(i);
	return clusters	

def train(X,k,eps):
	n,d = len(X),len(X[0])
	C = get_initial(X,k);
	while 1:
		clusters = create_clusters(X,C,n,k);
		nC = [];
		for j in xrange(k):
			m = max(1,len(clusters[j]));
			y = np.array([0]*d);
			for p in clusters[j]:
				y = y + X[p];
			y = np.true_divide(y,m + 0.0);
			nC.append(y);
		nC = np.array(nC);
		error = np.sum([np.sum((C[i] - nC[i])**2)  for i in xrange(k)])
		if error < eps : break;
		C = nC;
	return C;


def main():
	path_to_data = "/home/noureldin/Desktop/College/Data Mining/project 1/data.csv";
	with open(path_to_data, 'rb') as csvfile:
		csv_reader_object = csv.reader(csvfile);
		raw_data = [row for row in csv_reader_object];
		X = np.array([np.array(map(np.float64,row[:-7])) for row in raw_data]);
		Y = np.array([np.array(np.float64(row[-7:])) for row in raw_data]);
		C = train(X,7,1e-18);
		clusters = create_clusters(X,C,len(X),7)
		
		output = file("clusters.txt","w");			
		for i in xrange(len(clusters)):
			output.write(str(i + 1) + "\n");
			output.write(" ".join([str(point + 1) for point in clusters[i]]) + "\n");
			output.write("\n");
	
	
if __name__ == "__main__":
	main()
