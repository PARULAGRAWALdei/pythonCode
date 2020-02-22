import numpy as np
from matplotlib import pyplot as plt
import cv2


#importing the image file
img=cv2.imread('03.jpg',0)

#displaying original file
cv2.imshow('Original_image',img)

#calculating and plotting histogram using opencv
hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure(1)
plt.plot(hist)
plt.show()
eql=cv2.equalizeHist(img)
res=np.hstack((img,eql))
cv2.imshow('res',res)

#applying median blurring and displaying blurred image with original one
mdn=cv2.medianBlur(img,5)
res=np.hstack((img,mdn))
cv2.imshow('MedianBlur',res)
cv2.imwrite('Median_blur.png',res)

#image equalization
eql=cv2.equalizeHist(mdn)
hist1=cv2.calcHist([eql],[0],None,[256],[0,256])
plt.figure(2)
plt.plot(hist1)
plt.show()

cv2.waitKey(0);
