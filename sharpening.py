import cv2
import numpy as np

mask = np.asarray([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], dtype = np.float32)

filepath = './testsets/i3/frame11'
imgpath = filepath + '.jpg'
image = cv2.imread(imgpath)

sharp_img = cv2.filter2D(image, -1, mask)

savepath = filepath + '_sharp.png'

cv2.imwrite(savepath, sharp_img)
