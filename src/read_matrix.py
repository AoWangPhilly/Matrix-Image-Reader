import numpy as np
import cv2
import matplotlib.pyplot as plt


def predict_digit(digit, dim=(28, 28)):
    model = tf.keras.models.load_model('digit.model')
    digit = cv2.resize(digit, dim)
    digit = np.reshape(digit, (1, 28, 28))
    prediction = model.predict(digit)
    return np.argmax(prediction)


def draw_borders(fname: str = 'Pictures/m1.png'):
    img = cv2.imread(fname)

    img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_NEAREST)
    # kernel = np.ones((7, 7), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)
    # Turn image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use Gaussian blur to reduce # of noisy edges
    blur = cv2.GaussianBlur(src=gray, ksize=(13, 13), sigmaX=1)

    # Seperate foreground and background, results in clearer matrix
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 199, 25)

    # Cut the white space
    thresh = 255*(thresh < 128).astype(np.uint8)
    # coords = cv2.findNonZero(thresh)  # Find all non-zero points (text)
    # x, y, w, h = cv2.boundingRect(coords)  # Find minimum spanning bounding box
    # thresh = thresh[y:y+h, x:x+w]
    # img = img[y:y+h, x:x+w]

    # Find contours
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Remove the two brackets on the side
    contours = sorted(
        contours, key=lambda x: cv2.contourArea(x), reverse=True)[2:]

    contours = sorted(
        contours, key=lambda x: cv2.boundingRect(x)[0]*50 + cv2.boundingRect(x)[1]*200)
    for i, cnt in enumerate(contours):
        if cv2.contourArea(cnt) > 50:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(thresh, (x-7, y-7), (x+w+7, y+h+7), (255, 255, 255))
            digit = thresh[y-1:y+h+1, x-1:x+w+1]
            # roi = thresh[y:y+h, x:x+w]
            resized_digit = cv2.resize(
                digit, (18, 18), interpolation=cv2.INTER_AREA)
            # resized_digit = image_resize(digit, 18, 18)
            padded_digit = np.pad(
                resized_digit, ((5, 5), (5, 5)), "constant", constant_values=0)
            cv2.imshow('.', padded_digit)
            cv2.waitKey(0)


if __name__ == '__main__':
    draw_borders()
