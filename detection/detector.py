import cv2
import numpy
from messaging.email_provider import EmailProvider
from detection_file import DetectionFile

class Detector:

    def run_detection(self, file: DetectionFile):
        video = cv2.VideoCapture(file.get_full_name())

        while True:
            try:
                ret, image = video.read()
                if not ret:
                    break

                image = cv2.resize(image, (400,350))
                image = cv2.rotate(cv2.rotate(cv2.rotate(image, 0, cv2.ROTATE_90_CLOCKWISE), 0, cv2.ROTATE_90_CLOCKWISE), 0, cv2.ROTATE_90_CLOCKWISE)
                hog = cv2.HOGDescriptor()
                hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
                gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

                boxes, width = hog.detectMultiScale(gray_image)
                boxes = numpy.array([[x, y, x+w, y+h] for (x,y,w,h) in boxes])

                for(xA, yA, xB, yB) in boxes:
                    cv2.rectangle(image, (xA,yA), (xB, yB), (0,255,0), 2)
                    if(xA > 0 or yA > 0 or xB > 0 or yB > 0):
                        file.hasDetected = True
                        break

                if(file.hasDetected):
                    break

                cv2.imshow("Human recognition", image)

                if(cv2.waitKey(1) & 0xFF == ord('q')):
                    break
            except Exception as e:
                print(str(e))
        # cv2.waitKey(0)
        cv2.destroyAllWindows()