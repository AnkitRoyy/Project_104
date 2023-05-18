import cv2


img = cv2.imread("solar-system.jpg")

cv2.putText(img, "SUN", (20, 300), fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,  fontScale=1.3, color=(255, 255, 255), thickness=2)
cv2.putText(img, "Mercury", (110, 180), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.6, color=(255, 255, 255))
cv2.putText(img, "Venus", (190, 270), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.6, color=(255, 255, 255))
cv2.putText(img, "Earth", (290, 270), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.6, color=(255, 255, 255))
cv2.putText(img, "Mars", (380, 270), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.6, color=(255, 255, 255))
cv2.putText(img, "Jupiter", (560, 380), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.6, color=(255, 255, 255))
cv2.putText(img, "Saturn", (760, 330), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.6, color=(255, 255, 255))
cv2.putText(img, "Uranus", (970, 330), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.6, color=(255, 255, 255))
cv2.putText(img, "Neptune", (1120, 330), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.6, color=(255, 255, 255))
cv2.putText(img, "Moon", (325, 160), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.3, color=(255, 255, 255))

cv2.imshow("output", img)
cv2.waitKey(0)
