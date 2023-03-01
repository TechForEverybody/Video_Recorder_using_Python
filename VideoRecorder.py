import cv2

video=cv2.VideoCapture(0)

videoWriter=cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (640,480))


is_recording_started=False

while True:
    ret,frame= video.read()

    videoWriter.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(2)==ord('q'):
        break


video.release()
videoWriter.release()
cv2.destroyAllWindows()