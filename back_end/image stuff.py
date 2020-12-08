import os
import io
import PIL.Image as Image
import base64
from base64 import encodebytes
import codecs

#with open("C:/Users/User/Desktop/FIREFANS/back_end/test1.jpg", "rb") as image:
   # b64string = base64.b64encode(image.read())
   # print(b64string)
path="C:/Users/User/Desktop/FIREFANS/back_end/test1.png"
def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img
    #return pil_img.save(byte_arr, format='PNG')

#imageBytes="iVBORw0KGgoAAAANSUhEUgAAAuAAAACFCAIAAACVGtqeAAAAA3NCSVQICAjb4U/gAAAAGXRFWHRTb2Z0d2FyZQBnbm9tZS1zY3JlZW5zaG907wO/PgAAIABJREFUeJzsnXc81d8fx9+fe695rYwIaa"

#image = Image.open(io.BytesIO(imageBytes.encode(original, 'utf-8')

fh = open("imageToSave.txt", "w+")

fh.write(str(get_response_image(path)))
fh.close()

f = io.BytesIO(base64.b64decode(get_response_image(path) ))
pilimage = Image.open(f)
pilimage.save("test.png")
#print(bytearray(get_response_image(path)))