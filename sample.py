import cv2

# print(cv2.__version__)


# Read image in different mode

img = cv2.imread('lena.jpg', 0)
print(img)

# Draw line based on coordinated
img = cv2.line(img, (0, 0), (255, 255), 10)

# Show the image
cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:  # Escape Key
    cv2.destroyAllWindows()
elif k == ord('s'):  # S key
    cv2.imwrite('lena_copy_with_color222.jpg', img)

# Print Images properties
print(img.shape)  # returns a tuple of number of rows, columns and channels
print(img.size)  # returns total number of Pixels accessed
print(img.dtype)  # returns image datatype obtained

# write to a new file
