from PIL import Image
import pytesseract

text = pytesseract.image_to_string("Bonnaroo.jpeg")
print(text)
