import requests
from PIL import Image
from io import BytesIO
from moviepy.editor import VideoFileClip

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
      row.append(_rgb2scratch(rgb))
    image_data.append(row)
  return str(image_data)

def img_from_url(url, size):
  response = requests.get(url)
  img = Image.open(BytesIO(response.content))
  img = img.convert('RGB')
  return _process_frame(img, size)

def vid(filepath, fps=1, size=32):
    clip = VideoFileClip(filepath)
    clip = clip.resize((size, size)).set_fps(fps)
    frames_data = []
    for frame in clip.iter_frames(fps=fps, dtype="uint8"):
        pil_image = Image.fromarray(frame)
        frame_data = _process_frame(pil_image, size)
        frames_data.append(frame_data)
    
    clip.close()
    return frames_data
