# USAGE
# --face cascades/haarcascade_frontalface_default.xml --eye cascades/haarcascade_eye.xml --video video/adrian_eyes.mov


from pyimagesearch.eyetracker import EyeTracker
from pyimagesearch import imutils
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument('-f', '--face', required=True,
    help= 'path to where the face cascade resides')

ap.add_argument('-e', '--eye', required=True,
    help='path to where the eye cacade resides')
ap.add_argument('-v', '--video',
    help='path to the video file')
args = vars(ap.parse_args())


et = EyeTracker(args['face'], args['eye'])


if not args.get('video', False):
    camera = cv2.VideoCapture(0)

else:
    camera = cv2.VideoCapture(args['video'])


while True:
    (grabbed, frame) = camera.read()

    if args.get('video') and not grabbed:
        break

    frame = imutils.resize(frame, width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = et.track(gray)


    for rect in rects:
        cv2.rectangle(frame, (rect[0],rect[1]), (rect[2],rect[3]), (0,255,0), 2)



    cv2.imshow('Tracking', frame)


    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break



camera.release()
cv2.destroyAllWindows()
































