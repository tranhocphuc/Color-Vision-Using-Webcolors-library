from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
import argparse
import utils
import cv2 

#construct the argument parser and parse the argument 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument ("-c","--clusters",required = True, type = int , help ="# of clusters")
args = vars(ap.parse_args())

#Load image, converting from BGR to RGB in order to plot in matplotplib
image = cv2.imread(args["image"])
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#Display Image 
plt.figure()
plt.axis("off")
plt.imshow(image)

#reshape the image to be a list of pixels 
image = image.reshape((image.shape[0] * image.shape[1], 3))


#cluster the pixel indensity 
clt = KMeans(n_clusters=args["clusters"])
clt.fit(image)

hist = utils.centroid_historgram(clt)
bar,x= utils.plot_colors(hist,clt.cluster_centers_)
print (x)
requested_color = x
actualname,closestname = utils.get_color(requested_color)
print ("Actual color name: ",actualname,"Closest color name: ",closestname)

plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()