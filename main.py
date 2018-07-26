import pytesseract as pt
from PIL import Image
import csv
import cv2

image_name = 'test.png'
image1 = cv2.imread(image_name)
h, w, _ = image1.shape

# print(pt.image_to_string(image1))
boxes = pt.image_to_boxes(image1)

for b in boxes.splitlines():
    b = b.split(' ')
    image1 = cv2.rectangle(image1, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (255,255,255), -1)

# cv2.imshow(image_name, image1)
# cv2.waitKey()



# cv2.startWindowThread()
# cv2.namedWindow("preview")
# cv2.imshow("preview", image1)

new_image_name = "output_"+image_name
cv2.imwrite(new_image_name, image1)
# image1.save(new_image_name)

# new_Image = Image.open(new_image_name)
# new_Image.show()
