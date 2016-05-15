import csv
import numpy as np;
from random import shuffle,random,randint
import time
from NB import *;
from sklearn.metrics import precision_recall_fscore_support;
from sklearn.naive_bayes import GaussianNB

def rescale(x):
	return np.float64(x)/256.

D = {0:"apple",1:"leaf",2:"background"};

path_to_data = "/home/noureldin/Desktop/College/Data Mining/project 2/part2/data.csv";
with open(path_to_data, 'rb') as csvfile:
	csv_reader_object = csv.reader(csvfile);
	raw_data = [row for row in csv_reader_object];
	
	#shuffle data
	for i in xrange(1000) : shuffle(raw_data);	
	
	#convert data into numpy high precision floating point	
	X = np.array([np.array(map(rescale,row[:3])) for row in raw_data]);
	Y = np.array([np.array(int(row[3])) for row in raw_data]);
	n = len(X);
	
	#split data
	n_train = int(n*0.7);
	n_test  = n - n_train;
	X_train = X[:n_train];  X_test  = X[n_train:];
	Y_train = Y[:n_train];	Y_test  = Y[n_train:];	
	Y_train = [Y_train[j] - 1 for j in xrange(n_train)];
	Y_test  = [Y_test[j] - 1 for j in xrange(n_test)];
	print X_test;
	clf = NB(3);
	start_time = time.time()
	clf.train(X_train,Y_train);
	print("--- %s seconds ---" % (time.time() - start_time))	
	y_predict = clf.predict(X_test);
	print y_predict	
	
	#accuracy and recall
	re = clf.recall(Y_test,y_predict);
	print clf.accuracy(Y_test,y_predict);	
	for i in xrange(3):
		print re[i];	
	
	#compare with sklearn's accuracy
	clf2 = GaussianNB()
	clf2.fit(X_train,Y_train);
	print clf2.predict(X_test);	
	print clf2.score(X_test,Y_test)*100;
	
	#save data
	f = file("saved_data.csv","w");
	for i in xrange(n_test):
		f.write(" ,".join([str(int(x*256)) for x in X_test[i]]) + " ," + D[y_predict[i]] + "\n");

	#output 3 samples
	apple = [];
	leaf = [];
	background = [];
	for i in xrange(n_test):
		if y_predict[i] == 0: apple.append(X_test[i]);
		elif y_predict[i] == 1: leaf.append(X_test[i]);
		else : background.append(X_test[i]);
	print "apples :"	
	C = []	
	for i in xrange(3):
		while 1:
			x = randint(0,len(apple) - 1);
			if x not in C: break;
		print map(int,[y for y in apple[x]*256]);
		C.append(x);
	C = []	
	for i in xrange(3):
		while 1:
			x = randint(0,len(leaf) - 1);
			if x not in C: break;
		print map(int,[y for y in leaf[x]*256]);
		C.append(x);
	C = []	
	for i in xrange(3):
		while 1:
			x = randint(0,len(background) - 1);
			if x not in C: break;
		print map(int,[y for y in background[x]*256]);
		background.append(x);
