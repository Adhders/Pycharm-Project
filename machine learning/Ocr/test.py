from PIL import Image
import pytesseract


class Languages:
    CHS = 'chi_sim'
    CHT = 'chi_tra'
    ENG = 'eng'


def img_to_str(image_path, lang=Languages.ENG):
    return pytesseract.image_to_string(Image.open(image_path), lang)


print(img_to_str('42966.jpg', lang=Languages.ENG))