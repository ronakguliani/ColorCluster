import numpy as np
from sklearn.cluster import KMeans
import cv2


def get_top_colors(image_path, num_colors):
    # Load image and convert from BGR to RGB
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to a 2D array of pixels and 3 color values (RGB)
    pixels = image.reshape((-1, 3))

    # Use KMeans clustering to find the most dominant colors
    kmeans = KMeans(n_clusters=num_colors, random_state=0,
                    n_init=10).fit(pixels)

    # Get the colors and sort them by frequency
    colors = kmeans.cluster_centers_
    counts = np.bincount(kmeans.labels_)
    sorted_colors = colors[np.argsort(-counts)]

    # Convert the colors from RGB to hex format
    hex_colors = [RGB_to_HEX(color.astype(int)) for color in sorted_colors]

    # Return the top num_colors colors as hex codes
    return hex_colors[:num_colors]


def RGB_to_HEX(color):
    return '#{:02x}{:02x}{:02x}'.format(*color)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: python colors.py <image_path> <num_colors>")
    else:
        image_path = sys.argv[1]
        num_colors = int(sys.argv[2])
        top_colors = get_top_colors(image_path, num_colors)
        print(top_colors)
