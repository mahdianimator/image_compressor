from PIL import Image
import os
from time import sleep

try:
    user_input = input("Enter Your Image : ")

    img = Image.open(user_input)

    width, height = img.size

    new_size = (width//2, height//2)

    resized_img = img.resize(new_size)

    resized_img.save("compressed_image.jpg", optimize=True, quality=50)

    original_size = os.path.getsize(user_input)

    compress_size = os.path.getsize("compressed_image.jpg")

    print("Original Size : ", original_size)
    print("Compressed Size : ", compress_size)

except:
    print("Error")