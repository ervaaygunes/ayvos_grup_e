import cv2 as cv

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)

capture = cv.VideoCapture('Videos/catvideo.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(12) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()