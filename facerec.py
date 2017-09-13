import cv2
import sys
import os
import openface
import time
import numpy as np

def comprare(startfolder, simg):
    diffst = {}
    diffs = []
    for root, dirs, files in os.walk("./"+startfolder, topdown=False):
        for name in files:
            cfile = os.path.join(root, name)
            dval = compare_face(cfile, simg)
            diffst[dval] = cfile
            diffs.append(dval)
    print diffst[min(diffs)], "has the least differences:", min(diffs)

def facerec(imagePath):
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.imwrite("./evshit/"+imagePath, image)
    cv2.waitKey(0)

align = openface.AlignDlib("shape_predictor_68_face_landmarks.dat")
net = openface.TorchNeuralNet("nn4.small2.v1.t7", 96)

def getRep(imgPath):
    bgrImg = cv2.imread(imgPath)
    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
    start = time.time()
    bb = align.getLargestFaceBoundingBox(rgbImg)
    if bb is None:
        raise Exception("Unable to find a face: {}".format(imgPath))
    start = time.time()
    alignedFace = align.align(96, rgbImg, bb,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    if alignedFace is None:
        raise Exception("Unable to align image: {}".format(imgPath))
    start = time.time()
    rep = net.forward(alignedFace)
    return rep

def compare_face(img1, img2):
    d = getRep(img1) - getRep(img2)
    return np.dot(d, d)

comprare(sys.argv[1], sys.argv[2])
def facerec_for_yall():
    for root, dirs, files in os.walk("./"+startfolder, topdown=False):
        for name in files:
            cfile = os.path.join(root, name)
            facerec(cfile)
