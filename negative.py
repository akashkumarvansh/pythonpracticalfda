import cv2
import matplotlib.pyplot as plt

# Read color image
img = cv2.imread('flower.jpg')
img= cv2.resize(img, (800,600))
if img is None:
    print("Error: Image not found")
else:
    # Negative for color image
    negative = 255 - img

    cv2.imshow("Original Image", img)
    cv2.imshow("Negative Image", negative)
    plt.hist(img.ravel(), bins=256)
    plt.title("Histogram of Original Image")
    plt.show()
    plt.hist(negative.ravel(), bins=256)
    plt.title("Histogram of negative Image")
    plt.show()
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


   
