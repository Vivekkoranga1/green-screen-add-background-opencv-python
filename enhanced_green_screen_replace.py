import cv2
import numpy as np

foreground = cv2.imread("giraffe.jpeg")
background = cv2.imread("safari.jpeg")

h,w = foreground.shape[:2] #finding height and width of foreground image("giraffe.jpeg") using list slicing
#here we get height first because image stored in form of rows and columns and row contribute to height so we get height 

background = cv2.resize(background,(w,h))#see order of width and height confuses many but remember here width is expected first and then height in tuple form 

#now we are converting our image to different color model which is hsv(hue,saturation,value)
#In BGR model(BLUE,GREEN,RED) → color values are mixed
#In HSV → Hue directly represents the color (like green)
 
hsv = cv2.cvtColor(foreground,cv2.COLOR_BGR2HSV)

# Green ≈ Hue between 35 and 85 here array is in this format [H,S,V] 
lower_green = np.array([35, 40, 40]) #HUE IS 35 and saturation is 40 and brightness/value 40 ignoring to dull for greyish value 
upper_green = np.array([85, 255, 255])

#now we are extracting our object from green using this mask which ignore color from low_green to upper_green range
#Mask shows green as white and everything else as black
mask = cv2.inRange(hsv, lower_green, upper_green)

#see mask was black and white image (binary form so we are doing negation to find green background
mask_inverse = cv2.bitwise_not(mask)

#Here down two foreground looks confusing 
#cv2.bitwise_and() always needs two source images (src1, src2) mandatory
#then apply mask_inverse if mask_inv = 255 → keep pixel ,else If mask_inv = 0   → make pixel black  
fg = cv2.bitwise_and(foreground, foreground, mask=mask_inverse)

# Extract background area same like foreground
bg = cv2.bitwise_and(background, background, mask=mask)

#we are adding values of  fg and bg see background of fg is black [0,0,0] so background of safari is added
final_output =cv2.add(fg,bg)

cv2.imwrite("enhanced_converted_green_image.jpeg",final_output)

cv2.imshow("final_output",final_output)
cv2.waitKey(0)
cv2.destroyAllWindows()