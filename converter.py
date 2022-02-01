import os
import sys
from PIL import Image,ImageFilter

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not (os.path.exists(output_folder)):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    filtered_img = img.convert("")
    clean_name = os.path.splitext(filename)[0]
    filtered_img.save(f"{output_folder}{clean_name}.pdf")
    print("All Done!")
    
