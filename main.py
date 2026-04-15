import cv2


foreground = cv2.imread("giraffe.jpeg") #foreground image giraffe with green screen
background = cv2.imread("safari.jpeg") #background image jungle that we will place instead of green screen

#first let's find the r,g,b value of green screen

#print(foreground[0,0])[ 28 255  76] at location 0,0 green screen is present so i am finding there

#now check shape(height,width,channels) of foreground and background image both must be equal for a good and smooth image

#print(foreground.shape) (480, 852, 3) 
#print(background.shape) (800, 1200, 3)

#see both image are not equal so i will make background equal to the foreground  

foreground_height = foreground.shape[0]
foreground_width = foreground.shape[1]

resized_background = cv2.resize(background,(foreground_width,foreground_height))
#https://github.com/Vivekkoranga1/digital-image-processing-opencv-python here you can find resize image commit for more help



#now looping through each foreground pixel and changing green pixel who have value [ 28 255  76] to similar location background pixel value

#nested loop can be written in any way either range over foreground_width first or foreground_height first
for w in range(foreground_width):
    for h in range(foreground_height):
        pixel = foreground[h,w]
        
        #see 'if (pixel == [ 28,255,76])' this cannot be done because it is np.array which can result [TRUE TRUE TRUE] if pixel is also [ 28,255,76] or [TRUE FALSE TRUE]
        #if any two matches so it become confusing and code break so we are using np.array object method <np.arrayobject>.any()
        #which make it true if any value is true eg.[TRUE,TRUE,TRUE] any one of these is true 
        if (pixel == [ 28,255,76]).any():
            foreground[h,w] = resized_background[h,w]
            


cv2.imwrite("converted_green_image.jpeg",foreground)

cv2.imshow("converted_green_image",foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()

##it is good not best will improve it further in future