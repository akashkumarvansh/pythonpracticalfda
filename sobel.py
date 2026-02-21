import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image in grayscale
img = cv2.imread("car.jpg", cv2.IMREAD_GRAYSCALE)

# Sobel X and Y
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0,ksize=3)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1,ksize=3)

# Convert to uint8
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# Combine Sobel
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

# Display
titles = ['Image', 'Sobel X', 'Sobel Y', 'Sobel Combined']
images = [img, sobelX, sobelY, sobelCombined]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
