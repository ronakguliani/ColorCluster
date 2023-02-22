import numpy as np
from sklearn.cluster import KMeans
import cv2

# Load the image file
image = cv2.imread('test1.png')

# Convert the image to a numpy array
image = np.array(image, dtype=np.uint8)

# Reshape the array to a 2D array of pixels
pixels = image.reshape(-1, 3)

# Use KMeans clustering to cluster the pixels in the image into k clusters
kmeans = KMeans(n_clusters=3, random_state=0).fit(pixels)

# Get the center colors of the k clusters
center_colors = kmeans.cluster_centers_

# Sort the center colors by the number of pixels assigned to each cluster and return the top 3
counts = np.bincount(kmeans.labels_)
sorted_counts = np.argsort(counts)[::-1][:3]
dominant_colors = center_colors[sorted_counts]

# Convert the colors to hex values
dominant_colors_hex = ['#%02x%02x%02x' %
                       tuple(color.astype(int)) for color in dominant_colors]

# Print the result
print(dominant_colors_hex)
