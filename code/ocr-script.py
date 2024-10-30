from PIL import Image

import pytesseract

try:
    text = pytesseract.image_to_string(Image.new('RGB', (100, 30), color='white'))
    print("pytesseract is working! Detected text:", text)
except pytesseract.TesseractNotFoundError:
    print("Tesseract is not found. Ensure it's installed and in your PATH.")
