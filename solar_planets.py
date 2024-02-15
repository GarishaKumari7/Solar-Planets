import cv2
img=cv2.imread("solar-system.jpg")


cv2.putText(img, 
            "Sun",
            (20,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255), #BGR COLOR
            thickness=1
            )
cv2.putText(img, 
            "Mercury",
            (90,180),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255), #BGR COLOR
            thickness=1
            )
cv2.putText(img, 
            "Venus",
            (198,180),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255), #BGR COLOR
            thickness=1
            )
cv2.putText(img, 
            "Earth",
            (280,180),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255), #BGR COLOR
            thickness=1
            )
cv2.putText(img, 
            "Mars",
            (370,180),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255), #BGR COLOR
            thickness=1
            )
cv2.putText(img, 
            "Jupiter",
            (480,180),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255), #BGR COLOR
            thickness=1
            )
cv2.putText(img, 
            "Saturn",
            (660,180),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255), #BGR COLOR
            thickness=1
            )
cv2.putText(img, 
            "Uranus",
            (940,180),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255), #BGR COLOR
            thickness=1
            )
cv2.putText(img, 
            "Neptune",
            (1080,180),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255), #BGR COLOR
            thickness=1
            )
cv2.imshow("solar planets",img)
cv2.waitKey(0)
print(img)