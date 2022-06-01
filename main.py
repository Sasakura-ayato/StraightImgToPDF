import cv2
import datetime
import img2pdf
from PIL import Image
import os
from pathlib import Path
import glob
import tkinter as tk
from tkinter import ttk

capture = cv2.VideoCapture(0)
capture.set(3, 1920)
capture.set(4, 1080)
capture.set(5, 30)

def shot():
    fn = './img_' + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + '.png'
    # ret, img = capture.read()
    if ret == True:
        cv2.imwrite(fn, img)
        print('saved.')

def compile_pdf(outfn):
    pdfFileName = outfn + '.pdf'
    path = "."
    ext = ".png"

    with open(pdfFileName, "wb") as files:
        files.write(img2pdf.convert([i for i in os.listdir(path)if i.endswith(ext)]))
    delfiles = glob.glob('./*.png')

    for delfile in delfiles:
        os.remove(delfile)

def main():
    while True:
        ret, img = capture.read()
        cv2.imshow("Window", img)
        k = cv2.waitKey(1)
        if k == 27:
            compile_pdf('output')
            break
        if k == 32:
            shot()
  
if __name__ == '__main__':
    main()

capture.release()
cv2.destroyAllWindows()