import glob
import cv2
import os

directory = list(glob.glob('*/data/misaligned_images'))[0]
new_directory = list(glob.glob('*/data/aligned_images'))[0]
for file in os.listdir(directory):
    image = cv2.imread(directory+"/"+file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_otsu, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    kernel_size = 2
    ksize = (kernel_size, kernel_size)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize)
    threshold_filtered = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
    nonZeroCoordinates = cv2.findNonZero(threshold_filtered)
    imageCopy = image.copy()
    for point in nonZeroCoordinates:
        imageCopy = cv2.circle(imageCopy, (point[0][0], point[0][1]), 1, (255, 0, 0))

    box = cv2.minAreaRect(nonZeroCoordinates)
    boxPts = cv2.boxPoints(box)
    for i in range(4):
        pt1 = (int(boxPts[i][0]), int(boxPts[i][1]))
        pt2 = (int(boxPts[(i+1)%4][0]), int(boxPts[(i+1)%4][1]))
        cv2.line(imageCopy, pt1, pt2, (0,255,0), 2, cv2.LINE_AA)

    angle = box[2]
    if angle >= 45:
        angle = -(90 - angle)
    if angle < 45:
        angle = - angle
    h, w, c = image.shape
    scale = 1.
    center = (w/2., h/2.)
    M = cv2.getRotationMatrix2D(center, -angle, scale)
    rotated = image.copy()
    cv2.warpAffine(image, M, (w, h), rotated, cv2.INTER_CUBIC, cv2.BORDER_REPLICATE)
    cv2.imwrite(new_directory+"/"+file, rotated)
