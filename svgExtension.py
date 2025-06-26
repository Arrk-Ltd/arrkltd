import os

# Set the path to your target folder
folder_path = 'C:/websites/www.accenture.com/is/content/accenture'

# Loop through only files (not directories) in the folder
for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename)

    if os.path.isfile(full_path) and filename.endswith('.svg'):
        # Remove only the .svg extension
        new_filename = filename[:-4]  # Remove last 4 characters (".svg")
        new_full_path = os.path.join(folder_path, new_filename)
        os.rename(full_path, new_full_path)
        print(f'Renamed: {filename} -> {new_filename}')
