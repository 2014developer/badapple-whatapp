# Import Modules
try: from PIL.Image import open
except: from Image import open
from sys import stdout
from datetime import timedelta
from cv2 import VideoCapture, imencode, resize
from io import BytesIO

# Set Up Variables.
DATE_TIME = "01/01/2019 00:00"
PREFIX = "-"
AUTHOR = "Henry"

# Configure Bad Apple!! as ASCII Characters.
ASCII_CHARS = ['0', '1']

# Clip Variables
CLIP_FRAMES = 6571
CLIP_SECONDS = 219.0666
CLIP_MINUTES = CLIP_SECONDS/60

# Functions
def I2T(File):
	im = open(File)
	(w, h) = im.size
	mim = im.convert("1")
	data = list(mim.getdata())
	counter = 0
	field = True
	stdout.write(str(DATE_TIME + " - " + AUTHOR + ": "))
	for pixel in data:
		if field:
			if pixel > 127: stdout.write(ASCII_CHARS[1])
			else: stdout.write(ASCII_CHARS[0])
		counter = counter + 1
		if counter >= w:
			counter = 0
			if field: stdout.write("\n")
			field = not field

vidcap = VideoCapture('./video.mp4')
success, image = vidcap.read()
index = 0
while success:
    index += 1
    I2T(BytesIO(imencode(".jpg", resize(image, (24, 32), interpolation = 3))[1]))
    success, image = vidcap.read()