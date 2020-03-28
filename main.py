from PIL import ImageGrab
from PIL import Image
	
leftborder = L
rightborder = R
upborder = U
downborder = D
	
pic = ImageGrab.grab(bbox=(L,R,U,D))
pic.save(saveFileName)
