import cv2
import numpy as np
import matplotlib.pyplot as plt

flower = cv2.imread("Flower.jpg")
flower = cv2.resize(flower, (800,600))

s = flower.shape

flowerGray = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY)
flowerGray = cv2.convertScaleAbs(flowerGray, alpha=1.2, beta=80)

cv2.imshow('original', flowerGray)
cv2.waitKey(0)

################ Histogram ################

def Hist(image):
    H = np.zeros((256,1))
    s = image.shape

    for i in range(s[0]):
        for j in range(s[1]):
            k = image[i,j]
            H[k,0] = H[k,0] + 1

    return H

histg = Hist(flowerGray)

plt.plot(histg)
plt.title("Original Histogram")
plt.show()

################ Main Code ################

x = histg.reshape(1,256)
y = np.zeros((1,256))

for i in range(256):
    if x[0,i] == 0:
        y[0,i] = 0
    else:
        y[0,i] = i

# Get rmin and rmax
rmin = np.min(y[np.nonzero(y)])
rmax = np.max(y[np.nonzero(y)])

print("Min:", rmin, "Max:", rmax)

# Stretch mapping
stretch = np.round(((255-0)/(rmax-rmin))*(y-rmin))

stretch[stretch < 0] = 0
stretch[stretch > 255] = 255

# Apply mapping
stretched_img = flowerGray.copy()

for i in range(s[0]):
    for j in range(s[1]):
        k = flowerGray[i,j]
        stretched_img[i,j] = stretch[0,k]

################ New Histogram ################

histg2 = Hist(stretched_img)
cv2.imshow('original', flowerGray)
cv2.imshow('stretched', stretched_img)

plt.plot(histg, label="Original")
plt.plot(histg2, label="Stretched")
plt.legend()
plt.title("Histogram Comparison")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
