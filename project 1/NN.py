import csv
import numpy as np;
from random import shuffle,random
import neurolab as nl
import time

path_to_data = "/home/noureldin/Desktop/College/Data Mining/project 1/data.csv";
with open(path_to_data, 'rb') as csvfile:
	csv_reader_object = csv.reader(csvfile);
	raw_data = [row for row in csv_reader_object];
	
	#shuffle data
	for i in xrange(1000) : shuffle(raw_data);	
	
	#convert data into numpy high precision floating point	
	X = np.array([np.array(map(np.float64,row[:-7])) for row in raw_data]);
	Y = np.array([np.array(np.float64(row[-7:])) for row in raw_data]);
	n = len(X);
	
	#split data
	n_train = int(n*0.7);
	n_test  = n - n_train;
	X_train = X[:n_train];  X_test  = X[n_train:];
	Y_train = Y[:n_train];	Y_test  = Y[n_train:];	
	
	#build NN 
	NN = nl.net.newff([[-1, 1],[-1, 1],[-1, 1],[-1, 1],[-1, 1],[-1, 1],[-1, 1],[-1, 1],[-1, 1]], [50,50,50,7])
	
	#set the learning type to backpropagation with gradient descent
	NN.trainf = nl.train.train_gd
	
	# start training and measure the time
	start_time = time.time()
	NN.train(X_train,Y_train,epochs = 1400,show = 200,goal = 0.000001,lr = 0.01,adapt = True);
	print("--- %s seconds ---" % (time.time() - start_time))	
	
	# predict 
	NN_output = NN.sim(X_test);
	ctr = 0;
	for i in xrange(n_test):
		ctr += np.argmax(NN_output[i]) == np.argmax(Y_test[i]);
	print "training accuracy : " + str(ctr*100.0/n_test);
	
	# save all data
	train_data = file("train.csv","w");
	test_data = file("test.csv","w");
	output = file("NN_output.txt","w");
	for i in xrange(n_train): train_data.write(",".join([str(v) for v in raw_data[i]]) + "\n");
	for i in xrange(n_train,n): test_data.write(",".join([str(v) for v in raw_data[i]]) + "\n");
	for i in xrange(n_test): output.write(str(np.argmax(NN_output[i]) + 1) + "\n");
