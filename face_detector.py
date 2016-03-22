import cv2

'''
Face Detector: Detects faces in a image
classifier: haarcascade_frontalface_default.xml from OpenCV library
'''

# load classifier
classifier = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')

# load image
img = cv2.imread('test_image1.jpg')

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces
faces = classifier.detectMultiScale(gray, 1.3, 5)

# draw rectangles on image for every detected face
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)

# finally show image
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()