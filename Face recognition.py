import cv2
import cv2.face
from names import fetch_names_from_file


recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
recognizer.read('./trainer/trainer.yml')   #load trained model
cascadePath = "./haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


id = 1 #number of persons you want to Recognize


names = fetch_names_from_file("./names.txt") #names, leave first empty bcz counter starts from 0

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
# cam = cv2.VideoCapture('./WIN_20240210_13_55_34_Pro.mp4') #for video capture
cam.set(3, 640) # set video FrameWidht
cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# flag = True

while True:

    ret, img =cam.read() #read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.1,
        minNeighbors = 17,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
        if (accuracy < 85):
            id = names[id]
            accuracy_str = "  {0}%".format(round( accuracy))

        else:
            id = "unknown"
            accuracy_str = "  {0}%".format(round(accuracy-100))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy_str), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("Thanks for using this program, have a good day.")
names.clear()
cam.release()
cv2.destroyAllWindows()
