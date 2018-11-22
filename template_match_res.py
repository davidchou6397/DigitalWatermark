#coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8') 
import cv2
import numpy as np

template = cv2.imread('./static/watermark.jpg', 0)

f = open("result.txt", "w")
for k in range(0, 7):
    img_gray = cv2.imread('./static/regenerated_watermarks/watermark_img_'+str(k)+'.jpg', 0)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    f.write(str(res)+'\n')
f.close()
