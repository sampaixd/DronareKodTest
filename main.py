
###########imports###########
import cv2
import smtplib, ssl
from pynput import keyboard
import keyboard
from time import sleep
#############################


def sendmail():     #function that sends mail with picture
    print("picture")
    sleep(1)


def facetracking(faceCascade, imgGray):     #function that allows facetracking
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)   #detects faces
    for (x, y, w, h) in faces:  #draws all faces
        cv2.rectangle(imgGray, (x,y), (x+w, y+h),(255,0,255), 2)
    print("drawing facetracking")



def main():
    path = ("Pictures/face.jpg")    #gets image
    faceCascade = cv2.CascadeClassifier("Pictures/facetracking.xml")    #gets facetracking ai file
    img = cv2.imread(path)  #creates image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #creates gray image
    program = True  #program loop
    facetracking_on = False #bool to check if facetracking is on or off
    while program:
        if keyboard.is_pressed("f"):    #switches current state of facetracking_on when pressed
            facetracking_on = not facetracking_on
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #refreshes image in order to clear facetracking rectangle
        if keyboard.is_pressed("p"):                        #when not active
            sendmail()   #sends mail with picture when pressed
        if keyboard.is_pressed("q"):    #shuts down program
            program = False
        #with keyboard.Listener(buttoninput = on_press) as listener:
            #if buttoninput == "f":
        if facetracking_on:
            facetracking(faceCascade, imgGray)
        cv2.imshow("Image", img)
        cv2.imshow("Gray Image", imgGray)
        cv2.waitKey(0)


if __name__ == '__main__':
    main()
