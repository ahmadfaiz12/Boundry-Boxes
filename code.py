import os
from natsort import natsorted
import glob
import numpy as np
import cv2 as cv
import json

### Pass Folder Name of Masked Images

dirname="S3 CC 20190822 Session 2 Camera B - 20 Segmentation"
allDirs=glob.glob(dirname+"/*")
#Main_JSON={}
img_dic={}
for folder in allDirs:
    folderName=os.path.basename(folder)
    print(folderName)
    files=glob.glob(folder+'/*')
    natsorted(files)
    print(len(files))
    Single_Image_Player_BBoxs=[]
    
    for im in (files):
        img=cv.imread(im,0)
        if img is not None:
            vals=np.transpose(np.nonzero(img))
            if len(vals)!=0:
                Ymin,Xmin=np.amin(vals, axis=0)
                Ymax,Xmax=np.amax(vals, axis=0)
                bbox=[int(Xmin),int(Ymin),int(Xmax),int(Ymax)]
                Single_Image_Player_BBoxs.append(bbox)
                img_dic[folderName]=Single_Image_Player_BBoxs
with open("BoundingBox_jasons/"+dirname+'.json', 'w') as fp:
    json.dump(img_dic, fp)
