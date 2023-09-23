# File Arranger

Welcome to the File Arranger Python program! This Python script helps you organize files in a directory by moving them to specific folders based on their file extensions. It simplifies file management and keeps your directory clean and organized.

## How It Works 🛠️

The File Arranger script performs the following tasks:

1. **Initialization**: Reads a configuration file (`Data/files.json`) that defines the mapping of file extensions to folder names.

2. **User Input**: Prompts the user to enter the target directory where files need to be organized.

3. **File Scanning**: Scans the target directory and identifies files (excluding subdirectories).

4. **File Movement**: Moves each file to the appropriate folder based on its file extension, as defined in the configuration file.

5. **Cleanup**: Removes empty directories from the target directory after file organization.

## Features ✨

- **File Organization**: Automatically organizes files into folders based on their extensions.
- **Customizable**: You can customize the mapping of file extensions to folder names in the configuration file.
- **Error Handling**: The script handles common errors, such as existing directories and destination folder not found.

## Usage 🚀

To use the File Arranger Python script, follow these steps:

1. Run the script in a Python environment, preferably in the same directory where your files are located.

2. Enter the target directory where files need to be organized when prompted:

   ```python
   Enter your directory: /path/to/target_directory
   ```

3. The script will organize the files based on their extensions into the specified folders.

4. After organization, the script will remove empty directories from the target directory.

## Configuration 📝
You can customize the file organization by modifying the Data/files.json configuration file. This file defines the mapping of file extensions to folder names. Update this file to match your specific needs.

## License 📄
This script is provided under the MIT License - see the LICENSE file for details.

## Contact 📧
If you have any questions or need assistance with using the File Arranger script, please feel free to contact the script author.

Thank you for using the File Arranger! Enjoy keeping your files neatly organized. 📂🚀
