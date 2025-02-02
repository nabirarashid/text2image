from PIL import Image
import pytesseract

def extract_text(image_path, lang):
    img = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(img, lang=lang)
    return extracted_text

print(extract_text('image.png', 'eng'))
