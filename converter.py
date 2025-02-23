import requests
from PIL import Image
from io import BytesIO

def _rgb2scratch(rgb):
    r, g, b = rgb
    return r * 256**2 + g * 256 + b

def _process_frame(image, size):
  resized_img = image.resize((size, size))
  image_data = []
  for y in range(size):
    row = []
    for x in range(size):
      rgb = resized_img.getpixel((x, y))[:3]
      row.append(rgb2scratch(rgb))
    image_data.append(row)
  return image_data

def img_from_url(url):
  response = requests.get(url)
  img = Image.open(BytesIO(response.content))
  img = img.convert('RGB')
  return _process_frame(img, 32)
