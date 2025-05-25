import os
from PIL import Image

# Input folder (your existing folder)
input_folder = 'C:/Users/amant/OneDrive/Desktop/image resize/Alluvial soil'

# Output folder in the same directory where this script is located
output_folder = os.path.join(os.path.dirname(__file__), 'resized_images_64x64')

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
        try:
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img_resized = img.resize((64, 64))  # Resize to 64x64
            output_path = os.path.join(output_folder, filename)
            img_resized.save(output_path)
            print(f"Resized and saved: {filename}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
