import os
from shutil import move

# Define the directory categories and file extensions
DIRECTORY_CATEGORIES = {
    'Programming Files': {'ipynb', 'py', 'java', 'cs', 'js', 'vsix', 'jar', 'cc', 'ccc', 'html', 'xml', 'kt'},
    'Music': {'mp3', 'wav', 'wma', 'mpa', 'ram', 'ra', 'aac', 'aif', 'm4a', 'tsa'},
    'Videos': {'mp4', 'webm', 'mkv', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'm4p', 'm4v', 'wmv', 'mov', 'qt', 'flv', 'swf', 'avchd', 'avi', 'asf', 'rm'},
    'Pictures': {'jpeg', 'jpg', 'png', 'gif', 'tiff', 'raw', 'webp', 'jfif', 'ico', 'psd', 'svg', 'ai'},
    'Applications': {'exe', 'msi', 'deb', 'rpm'},
    'Compressed': {'zip', 'rar', 'arj', 'gz', 'sit', 'sitx', 'sea', 'ace', 'bz2', '7z'},
    'Documents': {'txt', 'pdf', 'doc', 'xlsx', 'ppt', 'pps', 'docx', 'pptx'},
    'Other': set()  # Category for extensions not defined
}

# Create folders for each category if they don't exist
def create_folders():
    for folder in DIRECTORY_CATEGORIES.keys():
        try:
            os.makedirs(folder, exist_ok=True)
            print(f'{folder:20} Created or already exists')
        except OSError as e:
            print(f'Error creating folder {folder}: {e}')

# Find the corresponding folder for a given file extension
def get_target_folder(extension):
    for folder, extensions in DIRECTORY_CATEGORIES.items():
        if extension in extensions:
            return folder
    return 'Other'

# Move files to their respective folders
def move_files():
    for filename in os.listdir():
        # Exclude hidden files, directories, and this script itself
        if filename.startswith('.') or os.path.isdir(filename) or filename == __file__:
            continue

        # Get the file extension and move the file to the corresponding folder
        _, extension = os.path.splitext(filename)
        extension = extension.lower().lstrip('.')  # Strip the dot and convert to lowercase
        target_folder = get_target_folder(extension)
        
        # Ensure the file is not already in the correct folder
        if target_folder and not os.path.exists(os.path.join(target_folder, filename)):
            move(filename, target_folder)
            print(f'Moved {filename} to {target_folder}')
        else:
            print(f'{filename} already exists in {target_folder} or no target folder found')

# Main execution flow
if __name__ == '__main__':
    create_folders()
    move_files()
