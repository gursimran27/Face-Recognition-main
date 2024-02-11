import cv2
import time
from names import getNameAndStore
import os

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'


# cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
#Haar Cascade classifier is an effective object detection approach

face_id = input("Enter a Numeric user ID  here:  ")
#Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)

getNameAndStore()

print(colors.CYAN+"generating samples, may take some time ....... "+colors.RESET)

count=0

path="./Akshay Kumar"
for filename in os.listdir(path): #Accessing the directory where images are stored
    filepath = os.path.join(path, filename)
    img=cv2.imread(filepath,0)#0->grey scale 1->color
    # converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #The function converts an input image from one color space to another
    faces = detector.detectMultiScale(img, 1.1, 9)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) #used to draw a rectangle on any image

        count+=1
            
        cv2.imwrite("./samples/face." + str(face_id) + '.' + str(count) + ".jpg", img[y:y+h,x:x+w])
            # To capture & Save images into the datasets folder

        # cv2.imshow('image', img) #Used to display an image in a window



print(colors.GREEN+"Samples generated now closing the program...."+colors.RESET)
cv2.destroyAllWindows()


