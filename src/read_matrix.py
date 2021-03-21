import numpy as np
import cv2

# def sort_contours(cnts, method="top-to-bottom"):
# 	# initialize the reverse flag and sort index
# 	reverse = False
# 	i = 0
# 	# handle if we need to sort in reverse
# 	if method == "right-to-left" or method == "bottom-to-top":
# 		reverse = True
# 	# handle if we are sorting against the y-coordinate rather than
# 	# the x-coordinate of the bounding box
# 	if method == "top-to-bottom" or method == "bottom-to-top":
# 		i = 1
# 	# construct the list of bounding boxes and sort them from top to
# 	# bottom
# 	boundingBoxes = [cv2.boundingRect(c) for c in cnts]
# 	(cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
# 		key=lambda b:b[1][i], reverse=reverse))
# 	# return the list of sorted contours and bounding boxes
# 	return (cnts, boundingBoxes)


def rescaleFrame(frame, scale=0.75):
    # Works with images, videos, and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    # Return frame and dimensions
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

def clean_image(fname: str = 'Pictures/m3.png'):
    img = cv2.imread(fname)
    kernel = np.ones((7, 7), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, np.ones((4, 4), dtype=np.uint8)) # Perform noise filtering
    blur = cv2.GaussianBlur(src=gray, ksize=(7, 7), sigmaX=1)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 199, 25)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    thresh = 255 * (thresh < 128).astype(np.uint8)
    coords = cv2.findNonZero(thresh)
    x, y, w, h = cv2.boundingRect(coords)  # Find minimum spanning bounding box
    rect = thresh[y:y+h, x:x+w]
    rect = rescaleFrame(rect, .5)
    cv2.imshow('rect', rect)
    cv2.waitKey(0)


def draw_borders(fname: str = 'Pictures/m1.png'):
    img = cv2.imread(fname)

    img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_NEAREST)
    # Turn image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use Gaussian blur to reduce # of noisy edges
    blur = cv2.GaussianBlur(src=gray, ksize=(7, 7), sigmaX=0)

    # Seperate foreground and background, results in clearer matrix
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 199, 25)

    # Cut the white space
    thresh = 255*(thresh < 128).astype(np.uint8)
    # coords = cv2.findNonZero(thresh)  # Find all non-zero points (text)
    # x, y, w, h = cv2.boundingRect(coords)  # Find minimum spanning bounding box
    # thresh = thresh[y:y+h, x:x+w]
    # img = img[y:y+h, x:x+w]

    cv2.imshow('Thresh', thresh)
    # Find contours
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Remove the two brackets on the side
    contours = sorted(
        contours, key=lambda x: cv2.contourArea(x), reverse=True)[2:]
    # contours = sort_contours(contours)[0]
    # contours = sort_contours(contours, method='left-to-right')[0]
    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255))
        roi = thresh[y:y+h, x:x+w]
        # cv2.imwrite(f'ye{i}.png', roi)
    cv2.imshow('norm', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    clean_image()
