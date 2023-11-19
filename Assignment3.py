"""
Question:
Consider the following Python program and its output. The program
 Reads an image file,
 Displays it on the screen,
 Separates the red, green, and blue components of the image in to three different matrices,
 Inverts the red, green, and blue matrices left right,
 Copies the modified red, green, and blue components back to the original image variable,
 Displays the modified image variable (that is inverted left right) onto the screen, and finally
 Saves the inverted image as a jpg image file in the computer hard drive




"""
#Import Python module to read, display, and write images
import cv2
'''
The function below extracts the red component of an image and returns it as a two dimensional list
'''
def getRedComponent(img):
 
 if len(img[0][0]) != 3:
    print("Attempting to return the red component from a non RGB image")
    print("Returning an empty matrix")
    return []
 else:
    imageHeight = len(img)
    imageWidth = len(img[0])
    R = [] #Red component matrix

    for i in range(imageHeight):
        row = []
        for j in range (imageWidth):
          pixel = img[i][j]
          row.append(pixel[0])
          R.append(row)
          return R
          
          
        

'''
The function below extracts the green component of an image and returns it as a two dimensional list
'''
def getGreenComponent(img):
 #PUT YOUR CODE HERE
'''
The function below extracts the blue component of an image and returns it as a two dimensional list
'''
def getBlueComponent(img):
 #PUT YOUR CODE HERE
'''
The function below inverts a two dimensional list left right
'''
def invertMatrixLeftRight(M):
 #PUT YOUR CODE HERE
'''
The function below updates an image with given red, blue, and green two dimensional lists
'''



def updateImage(img, R, G, B):
 for i in range(len(img)):
 for j in range(len(img[0])):
 pixel = [R[i][j], G[i][j], B[i][j]]
 img[i][j] = pixel
'''
The function below inverts an image left right
'''


def invertImageLeftRight(myImage):
  R = getRedComponent(myImage)
  G = getGreenComponent(myImage)
  B = getBlueComponent(myImage)
  invertMatrixLeftRight(R)
  invertMatrixLeftRight(G)
  invertMatrixLeftRight(B)
  updateImage(myImage, R, G, B)



#Main Program
#Please note that you are NOT allowed to modify or change any part of the given main program.
#You must use the given main program as it is given to you without any modification.
#Read image
myImage = cv2.imread("Lenna.png")
#Display image
cv2.imshow("Original Image", myImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Invert image left right
invertImageLeftRight(myImage)
#Display the inverted image
cv2.imshow("Inverted Image", myImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Save the inverted image in the computer hard drive
cv2.imwrite("Lenna_INVERTED.png", myImage)
