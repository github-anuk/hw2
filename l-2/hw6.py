import cv2
image=cv2.imread("pika2.png")

#cv2.copyMakeBorder(image, top, bottom, left, right, borderType, colorValue)
broderdimage =  cv2.copyMakeBorder(image, 10 ,10 ,10 ,10, cv2.BORDER_CONSTANT,value=1 )

cv2.imshow("bordered image",broderdimage)
cv2.waitKey(0)
cv2.destroyAllWindows()