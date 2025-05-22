import os
import shutil
import math

def distribute_files(source_folder, dest_folders):
    # Get all files from the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    total_files = len(files)
    
    # Calculate how many files per folder
    files_per_folder = math.ceil(total_files / len(dest_folders))
    
    print(f"Distributing {total_files} files into {len(dest_folders)} folders, approximately {files_per_folder} files per folder")
    
    # Create destination folders if they don't exist
    for folder in dest_folders:
        os.makedirs(folder, exist_ok=True)
    
    # Distribute files
    for i, folder in enumerate(dest_folders):
        start_idx = i * files_per_folder
        end_idx = start_idx + files_per_folder
        
        # For the last folder, take all remaining files
        if i == len(dest_folders) - 1:
            end_idx = total_files
        
        for file in files[start_idx:end_idx]:
            src_path = os.path.join(source_folder, file)
            dest_path = os.path.join(folder, file)
            shutil.move(src_path, dest_path)
        
        print(f"Moved {end_idx - start_idx} files to {folder}")

if __name__ == "__main__":
    # Configuration - modify these paths as needed
    source_folder = ".\soil_classification-2025\\train"  # Replace with your source folder path
    dest_folders = [
        "path/to/destination/Nioteshwar",
        "path/to/destination/Anish",
        "path/to/destination/Aman",
        "path/to/destination/Tejasvini"
    ]
    
    # Validate source folder
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist!")
        exit(1)
    
    # Run the distribution
    distribute_files(source_folder, dest_folders)
    print("File distribution completed!")