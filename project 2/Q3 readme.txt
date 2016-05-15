to extract the pixel values of image I wrote a script (pixel_extraction.py) which displays the image and reads the pixel values at positions where the mouse curser hit ,created a data of 73 instances and saves it in data.csv

after that the job was straightforward and a lot of the code was reused from Q2 
first I rescaled the input to be in range [0,1] and ran the classifier and here are the results and saved data in saved_data.csv


running time : 0.00058 seconds
accuracy :  82.14%

3 sample pixels predicted as apples :
[118, 24, 25]
[108, 2, 4]
[123, 27, 31]

3 sample pixels predicted as leaf:
[143, 166, 36]
[171, 189, 81]
[136, 160, 20]


3 sample  pixels predicted as background:
[219, 126, 134]
[192, 205, 117]
[255, 255, 255]
