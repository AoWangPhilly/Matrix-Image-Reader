import numpy as np
import cv2


def draw_borders(fname: str = 'Pictures/m2.jpeg'):
    img = cv2.imread(fname)

    # Turn image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use Gaussian blur to reduce # of noisy edges
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Seperate foreground and background, results in clearer matrix
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 199, 25)

    # Find contours
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow('Thresh', thresh)
    cv2.waitKey(0)

if __name__ == '__main__':
    draw_borders()