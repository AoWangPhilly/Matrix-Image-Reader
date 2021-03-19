import numpy as np
import cv2


def draw_borders(fname: str = 'Pictures/m3.png'):
    img = cv2.imread(fname)
    
    img = cv2.resize(img, (255, 255), interpolation = cv2.INTER_NEAREST)
    # Turn image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use Gaussian blur to reduce # of noisy edges
    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    # Seperate foreground and background, results in clearer matrix
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 199, 25)

    cv2.imshow('Thresh', thresh)
    # Find contours
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        c_area = cv2.contourArea(cnt)
        if  c_area > 100 and c_area < 800:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)
        # roi = thresh[y:y+h, x:x+w]

    cv2.imshow('norm', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    draw_borders()