# Color Dominance

This project is designed to identify the dominant colors present in an image and output the hex code for those colors. The algorithm used in this project utilizes K-means clustering to group similar colors together, then identifies the most prevalent colors in each cluster to determine the dominant colors in the image.

## Features

- Identifies the most prevalent colors in an image
- Outputs the hex codes for the dominant colors
- Supports JPG, PNG, and other common image formats

## Installation

To use this project, first clone the repository to your local machine. Then, install the required dependencies using pip:
> pip install numpy opencv-python scikit-learn

## Usage

> python colors.py [path_to_image_file] [number_of_colors]

This will output a list of hex codes representing the dominant colors in the image.

## Future Work

- Improved color accuracy
- Integration with other image processing libraries
- Gradients

## License

This project is licensed under the MIT License.
