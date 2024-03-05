import cv2 

img = cv2.imread("pika1.png",1)
cv2.imshow("OG ",img)

Gaussian = v=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("gaussian bluring",Gaussian)

median = v=cv2.medianBlur(img,5)
cv2.imshow("median blur",median)


bilateral = v=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bilateral bluring",bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

bilateral = v=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bilateral bluring",bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows() 