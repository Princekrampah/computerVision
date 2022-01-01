import cv2

video = cv2.VideoCapture(0)
if video.isOpened():
   while True:
        check, frame = video.read()
        if check:
            cv2.imshow('Color Frame', frame)
            key = cv2.waitKey(50)

        if key == ord('q'):
            break
        else :
            print('Frame not available')
            print(video.isOpened())


            