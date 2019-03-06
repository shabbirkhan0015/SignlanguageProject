from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = Image.open("image.png")## path of image
text = pytesseract.image_to_string(img)
print(text)