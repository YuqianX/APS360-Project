from image_cascadeClassifier import *
from mask_analysis import *
from video_integration import *
import cv2

def integrated_system():
    analyzer=mask_analysis_system()
    face_finder=cv2.CascadeClassifier('haarcascade_eye.xml')
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()

        try:
            coordinate_list = getFaceCoordinates(img, face_finder)

            face_list = getListOfFaces(img, coordinate_list)
            judge_list = analyzer.analysis(face_list)
            video_integration(img, coordinate_list, judge_list)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        except:
            print("oop!")

integrated_system()

