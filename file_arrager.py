# IMPORTS

import os
import string
import json
import shutil

# File Arranger object class


class arranger():
    def __init__(self):
        self.file_class = "Data/files.json"
        with open(self.file_class) as f:
            self.files_list = json.load(f)
        self.dir_names = list(self.files_list.keys())
        print()
        self.directory = str(input("Enter your directory: "))
        print()

    def get_files(self):
        files = os.listdir(self.directory)
        files = [
            file
            for file in files
            if not os.path.isdir(os.path.join(self.directory, file))
        ]
        exceptions = ['desktop.ini']
        files = [x for x in files if x not in exceptions]
        return files

    def dir_make(self):

        for name in self.dir_names:
            file_dir = self.directory + name
            try:
                os.mkdir(file_dir)
            except:
                print(f"[{file_dir} already exists!]")

    def get_extension(self, file):
        length = len(file)
        for i in range(length - 1, -1, -1):
            if file[i] == ".":
                return file[i:]
        return ""

    def is_empty(self, directory): 
        return len(os.listdir(directory)) == 0

    def rm_empty_dirs(self):
        for entry in os.scandir(self.directory):
            file_path = os.path.join(self.directory, entry)
            empty = self.is_empty(file_path)
            if entry.is_dir():
                if empty:
                    try: 
                        os.rmdir(file_path)
                    except: 
                        print(f"Error: Failed to remove directory '{directory}'. {e}")



    def mv_files(self):
        self.dir_make()
        files = self.get_files()
        for file in files:
            ext = self.get_extension(file)
            src_path = os.path.join(self.directory, file)
            ext_confirmation = any(
                ext in self.files_list[key] for key in self.dir_names)
            dest_dir = None
            if ext_confirmation == True:
                try:
                    for key in self.dir_names:
                        if ext in self.files_list[key]:
                            dest_dir = os.path.join(self.directory, key)
                            break
                except:
                    print(f"[Error moving files]")
            else:
                dest_dir = os.path.join(self.directory, 'miscellaneous')
            if dest_dir is not None:
                shutil.move(src_path, dest_dir)
                print(f"[Moved {file} To {dest_dir}]")
            else:
                print(f"[Error: Destination directory not found for {file}]")
        self.rm_empty_dirs()
