import os
from PIL import Image

input_folder = "input_images"
output_folder = "output_images"
max_size = (800, 800)  # Max width and height
output_format = "JPEG"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        path = os.path.join(input_folder, file)
        with Image.open(path) as img:
            img = img.convert("RGB")  # ensures compatibility with JPEG
            img.thumbnail(max_size)  # preserves aspect ratio

            base_name = os.path.splitext(file)[0]
            out_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
            img.save(out_path, output_format)

            print(f"Saved: {out_path}")

print(" All images resized with aspect ratio!")
