import cv2
import os

'''
This script is to help you to generate a haar casscade classifier with ease.
Steps:
1. Put positive images in pos folder. Images should be of same dimensions.
2. Put negative_images(background images) in neg folder. 
	Background images should be of larger size than positive images.
3. Create a data folder which will contain all cascade and classifier files.
4. Change Paramters based on your number of positive and negative images.
'''

# Directory with positive images
dir_pos_name = "pos"

# Directory with negative images
dir_neg_name = "neg"

# Dimension of samples
image_width = "20"
image_height = "20"

# Name of files to contain list of images in respective folders
file_pos_name = "positive_images.info"
bg_file = "bg.txt"

number_of_samples = "1000" # Number of samples you want to generate
width = "20" 
height = "20"  

vector_file_name = "samples.vec"

data_folder = "data"
numStages = "50"
nsplits = "2"
minhitrate = "0.999"
maxfalsealarm = "0.5"

# numPos and numNeg are number of samples it takes for every stage.
numPos = "1000"
numNeg = "1000" 

'''
Commands
'''
# find pos -iname "*.*" -exec echo \{\} 1 0 0 100 40 \; > positive_images.info

# find neg -iname "*.*" > bg.txt

# opencv_createsamples -info positive_images.info -num 550 -w 48 -h 24 -vec samples.vec

# opencv_traincascade -data data -vec samples.vec -bg bg.txt -numStages 10 -nsplits 2 -minhitrate 0.999 -maxfalsealarm 0.5 -numPos 500 -numNeg 500 -w 48 -h 24

'''
This method is to format a command which will list all images from pos folder 
into "positive_images.info" file with number of objects and position of objects 
in corresponding image.
'''
def create_command(dir_pos_name, image_width, image_height, file_pos_name):
	command = "find "+dir_pos_name+" -iname \"*.*\" -exec echo \{\} 1 0 0 "+image_width+" "+image_height+" \; > "+file_pos_name
	return command

'''
This method is to format a command which will create a file "bg.txt" containing 
list of images in neg folder (one image per line).
'''
def create_command1(dir_neg_name, bg_file):
	command = "find "+dir_neg_name+" -iname \"*.*\" > "+bg_file
	return command

'''
This method is to format a command which will create positive samples out of 
positive_images and background images.
'''
def create_command2(file_pos_name, number_of_samples, width, height, vector_file_name):
	command = "opencv_createsamples -info "+file_pos_name+" -num "+str(number_of_samples)+" -w "+str(width)+" -h "+str(height)+" -vec "+vector_file_name
	return command

'''
This method is to format a command which will train a casscade classifier.
'''
def create_command3(data_folder, vector_file_name, bg_file, numStages, nsplits, minhitrate, maxfalsealarm, numPos, numNeg, width, height):
	command = "opencv_traincascade -data "+data_folder+" -vec "+vector_file_name+" -bg "+bg_file+" -numStages "+numStages+" -nsplits "+nsplits+" -minhitrate "+minhitrate+" -maxfalsealarm "+maxfalsealarm+" -numPos "+numPos+" -numNeg "+numNeg+" -w "+width+" -h "+height
	return command

'''
Create commands
'''
command1 = create_command(dir_pos_name, image_width, image_height, file_pos_name)
command2 = create_command1(dir_neg_name, bg_file)
command3 = create_command2(file_pos_name, number_of_samples, width, height, vector_file_name)
command4 = create_command3(data_folder, vector_file_name, bg_file, numStages, nsplits, minhitrate, maxfalsealarm, numPos, numNeg, width, height)

# Run commands 
os.system(command1)
os.system(command2)
os.system(command3)
os.system(command4)