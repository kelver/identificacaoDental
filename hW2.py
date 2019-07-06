import cv2

# Image file
IMAGE_FILE = '4.jpg' # Change this to be your image

# Cascade file
CASCADE_FILE = 'cascadefina.xml'

# Load image file
image = cv2.imread(IMAGE_FILE)

# Convert the image to gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
color = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Load your cascade file
cascade = cv2.CascadeClassifier(CASCADE_FILE)
eyes = cascade.detectMultiScale(gray)

for (ex,ey,ew,eh) in eyes:
	cv2.rectangle(color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# Display the cascade to the user
cv2.imshow("s", image)
cv2.imwrite("s.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()