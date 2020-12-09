import os
import cv2
import pandas as pd
import numpy

# get data 
img = cv2.imread(os.path.join('data', 'colorpic.jpg'))
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
colors = pd.read_csv(os.path.join('data', 'colors.csv'), names=index, header=None)

# set global vars
clicked = False
r = g = b = xpos = ypos = 0

# function to get name of RGB vals by finding min distance d to nearest color
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, 'R'])) + abs(G - int(colors.loc[i, 'G'])) + abs(B - int(colors.loc[i, 'B']))
        if (d <= minimum):
            minimum = d
            color_name = colors.loc[i, 'color_name']
    return color_name

# draw function will use mouse coordiantes to calculate RGB when doubble clicked
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,cpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

# set mouse callback event for a window
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

# display image
while(1):
    
    cv2.imshow('image', img)
    
    if (clicked):

        # fills rectangle with image (image, startpoint, endpoint, color, thickness)-1
        cv2.rectangle(img, (20,20), (750,60), (b,g,r), -1)
        # create display string to show color name and RGB vals
        text = getColorName(r,g,b) + 'R=' + str(r) + 'G=' + str(g) + 'B=' + str(b)
        # format 
        cv2.putText(img, text, (50,50), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)
        # if color is very light, display black text instead 
        if(r+g+b >= 600):
            cv2.putText(img, text, (50,50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)
            
        clicked = False

    # break loop if user hits 'esc'
    if cv2.waitKey(20) & 0xFF==27:
        break

cv2.destroyAllWindows()





        
