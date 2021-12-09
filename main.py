import cv2 as cv
import numpy as np
import pytesseract
import re


def find_coord_donate_seeds(img):
    # Закрашиваем ненужные области
    img[0:200, 0:1920] = (0, 0, 0)
    img[800:1080, 0:1920] = (0, 0, 0)

    # Находим необходимый цвет
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower_blue = np.array([108, 50, 50])
    upper_blue = np.array([114, 255, 255])
    threshold = cv.inRange(hsv, lower_blue, upper_blue)

    # Фильтруем и убираем шумы
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (50, 5))
    threshold = cv.morphologyEx(threshold, cv.MORPH_CLOSE, kernel)
    threshold = cv.erode(threshold, kernel, iterations=1)
    threshold = cv.dilate(threshold, kernel, iterations=1)

    # Находим координаты кнопки сдачи семян
    contours, hierarchy = cv.findContours(threshold.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    donate_seeds = contours[0]
    M = cv.moments(donate_seeds)
    cx = int(M['m10']) / M['m00']
    cy = int(M['m01']) / M['m00']
    return cx, cy


def check_for_person(img):
    def find_arithmetic_text(img):
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string(img_rgb, lang='rus')
        regex = re.compile(r'Сколько будет (\d+) \+ (\d+)?')
        result = regex.search(text)
        print(result)
        first_number = result.group(1)
        second_number = result.group(2)
        return (first_number, second_number)

    def calculation(numbers):
        answer = int(numbers[0]) + int(numbers[1])
        return answer

    numbers = find_arithmetic_text(img)
    return calculation(numbers)