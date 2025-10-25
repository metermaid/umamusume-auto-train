import pytesseract
from PIL import Image
import numpy as np
import re
import logging

def extract_text(pil_img: Image.Image) -> str:
  img_np = np.array(pil_img)
  result = pytesseract.image_to_string(img_np, config= "--psm 6")
  result = re.sub(r"\n", " ", result)
  return result

def extract_number(pil_img: Image.Image) -> int:
  img_np = np.array(pil_img)
  result = pytesseract.image_to_string(img_np, config= "--psm 7 -c tessedit_char_whitelist=0123456789%")

  digits = re.sub(r"[^\d]", "", result)
  if digits:
    return int(digits)
  
  return -1
