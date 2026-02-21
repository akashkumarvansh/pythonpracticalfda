import cv2
import matplotlib.pyplot as plt


img = cv2.imread('fl.jpg', 0)

equalized = cv2.equalizeHist(img)

cv2.imshow("Original", img)
cv2.imshow("Equalized", equalized)

plt.hist(img.ravel(), bins=256)
plt.title("Histogram of Original Image")
plt.show()
plt.hist(equalized.ravel(), bins=256)
plt.title("Histogram of equalized Image")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
