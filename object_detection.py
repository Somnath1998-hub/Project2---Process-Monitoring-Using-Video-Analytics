# import all necessary packages
import cv2
import numpy as np


class chess_detection():
	"""
	This class is defined to get the loactions of 8*8 grid of chess board and the piecess on board
	"""
	def __init__(self):
		pass

	def get_location(self, image, draw = True):
		"""
		Input : image, draw
		Output : locations
	
		This method takes chess board image as input and finds the location of 8*8 grid on chess board by 
		deviding height and weidth in 8 equal parts 
		"""
		# height, width, number of channels in image
		height = image.shape[0]
		width = image.shape[1]
		channels = image.shape[2]

		# split height and width into 8 equal parts
		def split_into_parts(number, n_parts):
		    return np.linspace(0, number, n_parts+1)[1:]

		h = split_into_parts (height, 8)
		w = split_into_parts (width, 8)

		# add initial point loaction
		h =np.insert(h,0,0)
		w =np.insert(w,0,0)

		# get loactions list - top left corner and bottom right corner
		i = 0 
		locations = []
		while i<8:
		    j = 0
		    
		    while j <8:
		        b = []
		        b.append( (int(w[j]), int(h[i]) ))
		        b.append( (int(w[j+1]), int(h[i+1])) )
		        j +=1
		        locations.append(b)
		        
		    i+=1
		# draw the loaction if True
		if draw:
			for i in range(len(locations)):
				image =cv2.rectangle(image, locations[i][0], locations[i][1], (0,0,255), 1)
		return locations