import cv2
img=cv2.imread("pi.jpeg")
print(img)
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('grey.jpg',gry)
print(gry)