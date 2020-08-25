import numpy as np
import cv2
import math
from matplotlib import pyplot as plt


def otsu(input):


    his, bins = np.histogram(input, np.array(range(0, 256)))
    h, w = input.shape

    threshhold = 100
    val = 20


    for x in range(1,255):
        Wb = h*w*np.sum(his[:x])
        Wf = h*w*np.sum(his[x:])
        m1 = np.mean(his[:x])
        m2 = np.mean(his[x:])
        m = (Wb*Wf*(m1 - m2))** 2
        if m > val:
            threshhold = x
            val = m



    output = input.copy()
    print("threshhold is :")
    print(threshhold)

    output[input > threshhold] = 255
    output[input < threshhold] = 0

    return output


image = cv2.imread('redBall.png',0)
img = otsu(image);
cv2.imwrite('utso.png', img)




#put  value for  different threshold

#th = 50
output = image.copy()

output[image > 50] = 255
output[image < 50] = 0
plt.plot(122),plt.imshow(output, cmap = 'gray')
plt.title(" output for threshold 50"), plt.xticks([]), plt.yticks([])
plt.show();

#th = 200
output[image > 200] = 255
output[image < 200] = 0
plt.plot(122),plt.imshow(output, cmap = 'gray')
plt.title(" output for threshold 200"), plt.xticks([]), plt.yticks([])
plt.show();


#th = 170
output[image > 170] = 255
output[image < 170] = 0
plt.plot(122),plt.imshow(output, cmap = 'gray')
plt.title(" output for threshold 170"), plt.xticks([]), plt.yticks([])
plt.show();

#th = 30
output[image > 30] = 255
output[image < 30] = 0
plt.plot(122),plt.imshow(output, cmap = 'gray')
plt.title(" output for threshold 20"), plt.xticks([]), plt.yticks([])
plt.show();


plt.plot(122),plt.imshow(img, cmap = 'gray')
plt.title("utso output (132)"), plt.xticks([]), plt.yticks([])
plt.show();