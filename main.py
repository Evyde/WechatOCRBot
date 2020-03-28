from PIL import ImageGrab
from PIL import Image
import win32api

#框选
leftborder = L
rightborder = R
upborder = U
downborder = D
#确定main.py中的L,R,U,D值
x=win32api.GetSystemMetrics(0)
y=win32api.GetSystemMetrics(1)
l=0.2803*x
r=0.5872*x
u=0.6728*y
d=0.7340*y
L=int(l)
R=int(r)
U=int(u)
D=int(d)

#截图
pic = ImageGrab.grab(bbox=(L,R,U,D))
pic.save(saveFileName)
