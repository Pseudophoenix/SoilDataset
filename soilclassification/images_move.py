import os
import shutil
import pandas as pd

# Read the CSV file
df = pd.read_csv('.\soilclassification2025\\train_labels.csv')

# Directory where the images are currently stored (change this to your actual directory)
source_dir = '.\soilclassification2025\\train'  # Replace with your actual path

# Create destination folders for each soil type if they don't exist
soil_types = df['soil_type'].unique()
for soil_type in soil_types:
    os.makedirs(os.path.join(source_dir, soil_type), exist_ok=True)

# Move each file to its respective folder
for index, row in df.iterrows():
    src_path = os.path.join(source_dir, row['image_id'])
    dst_path = os.path.join(source_dir, row['soil_type'], row['image_id'])
    
    try:
        shutil.move(src_path, dst_path)
        print(f"Moved {row['image_id']} to {row['soil_type']} folder")
    except FileNotFoundError:
        print(f"File not found: {row['image_id']}")
    except Exception as e:
        print(f"Error moving {row['image_id']}: {str(e)}")

print("File organization completed!")