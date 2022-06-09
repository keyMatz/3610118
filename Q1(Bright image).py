import cv2
import numpy as np

img = cv2.imread('AOT.png', -1)
cv2.imshow("Original image", img)
Intensity_Matrix = np.ones(img.shape, dtype = "uint8") * 100

print(Intensity_Matrix)

brightened_image = cv2.add(img, Intensity_Matrix)
cv2.imshow("Bright", brightened_image)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('AOT_copy.png', img)
    cv2.destroyAllWindows()