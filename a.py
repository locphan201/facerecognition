import cv2

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
fps = 60
index = 1
while True:
    check, frame = video.read()
    
    frame = cv2.flip(frame, 1)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=4)
    
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
    cv2.imshow('Video', frame)
    key = cv2.waitKey(int(1000/fps))
    
    if key == ord('q'):
        break
    
video.release() 
cv2.destroyAllWindows()