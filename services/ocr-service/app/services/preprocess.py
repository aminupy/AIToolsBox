import pytesseract
import cv2
import numpy as np
from PIL import Image
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
BASE_DIR = r"C:\D\program\AiToolBox\AIToolsBox\services\ocr-service\app\services"
image_path = os.path.join(BASE_DIR, "sample.png")
image = Image.open(image_path)
img = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

kernel = np.ones((3, 3), np.uint8) 


dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

extracted_text = pytesseract.image_to_string(dilated_image)
print(extracted_text)