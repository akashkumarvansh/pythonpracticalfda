import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image in grayscale
img = cv2.imread("football.jpg", 0)

# Apply Canny Edge Detection
canny = cv2.Canny(img, 100, 200)

# Show Images
titles = ['Original Image', 'Canny Edge']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
