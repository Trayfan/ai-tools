import pytesseract
from PIL import Image

class GetText:
    def get_text(self, image_name):
        text_result = pytesseract.image_to_string(Image.open(image_name))
        return text_result
    