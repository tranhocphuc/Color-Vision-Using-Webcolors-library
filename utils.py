import numpy as np 
import cv2 
import webcolors
from skimage.color import rgb2lab, deltaE_cie76
import array

def centroid_historgram (clt):
    #grab the number of different clusters and create a histogram based on the number of pixels assigned to each cluster 
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)
 
	# normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()
	# return the histogram
    return hist

def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
	# of each of the colors
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0
	# loop over the percentage of each cluster and the color of each cluster
	
	for (percent, color) in zip(hist, centroids):
		# plot the relative percentage of each cluster
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
			color.astype("uint8").tolist(), -1)
		startX = endX
	return bar,color

def closest_colors(color):
    min_color ={}
    for key,name in webcolors.css3_hex_to_names.items():
        r_c,g_c,b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - color[0]) ** 2
        gd = (g_c - color[1]) ** 2
        bd = (b_c - color[2]) ** 2
        min_color[(rd + gd + bd)] = name
    return min_color[min(min_color.keys())]

def get_color(color): 
    try:
         closestname = actualname = webcolors.rgb_to_name(color)
    except ValueError: 
        closestname = closest_colors(color)
        actualname = None
    return actualname, closestname

