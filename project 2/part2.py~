import csv
import numpy as np;
from random import shuffle,random
import time
from NB import *;
from sklearn.metrics import precision_recall_fscore_support;
from sklearn.naive_bayes import GaussianNB

def rescale(x):
	return np.float64(x)

path_to_data = "/home/noureldin/Desktop/College/Data Mining/project 1/data.csv";
with open(path_to_data, 'rb') as csvfile:
	csv_reader_object = csv.reader(csvfile);
	raw_data = [row for row in csv_reader_object];
	
	#shuffle data
	for i in xrange(1000) : shuffle(raw_data);	
	
	#convert data into numpy high precision floating point	
	X = np.array([np.array(map(rescale,row[:-7])) for row in raw_data]);
	Y = np.array([np.array(np.float64(row[-7:])) for row in raw_data]);
	n = len(X);
	
	#split data
	n_train = int(n*0.7);
	n_test  = n - n_train;
	X_train = X[:n_train];  X_test  = X[n_train:];
	Y_train = Y[:n_train];	Y_test  = Y[n_train:];	
	Y_train = [np.argmax(Y_train[j]) for j in xrange(n_train)];
	Y_test  = [np.argmax(Y_test[j]) for j in xrange(n_test)];
	#print X_test;
	clf = NB(7);
	start_time = time.time()
	clf.train(X_train,Y_train);
	print("--- %s seconds ---" % (time.time() - start_time))	
	y_predict = clf.predict(X_test);
	re = clf.recall(Y_test,y_predict);
	print clf.accuracy(Y_test,y_predict);
	
	for i in xrange(7):
		print re[i];	
	
	# code to compare my impelementation's accuracy to that of the sklearn	
	clf2 = GaussianNB()
	clf2.fit(X_train,Y_train);
	#print clf2.predict(X_test);	
	print clf2.score(X_test,Y_test)*100;

	# save data
	out = file("predictions_task_2.csv","w");
	for i in xrange(n_test):
		out.write(" ,".join([str(x) for x in X_test[i]]) + " ," + str(y_predict[i]) + "\n");
