import json
import shutil
import os
import traceback
from pathlib import Path

class Initializer:

    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    def print_exception_info(self, e: Exception) -> None:
        print("\n--- Exception Occurred ---")
        print(f"Type    : {type(e).__name__}")
        print(f"Message : {e}")
        print("Traceback (most recent call last):")
        traceback.print_tb(e.__traceback__)
        print("---------------------------\n")
    
    def make_dirs(self, project_path: str, dirs: list) -> None:
        for my_dir in dirs:
            new_path = os.path.join(project_path, my_dir)
            Path(new_path).mkdir()
        
    def copy_files(self, project_path: str, files_path: str, config_files: list) -> None:
        for file in config_files:
            file_path_src = os.path.join(files_path, file["name"])
            file_path_dst = project_path

            for my_dir in file["path"]:
                file_path_dst = os.path.join(file_path_dst, my_dir)
            file_path_dst = os.path.join(file_path_dst, file["name"])

            Path(file_path_dst).touch()
            shutil.copyfile(file_path_src, file_path_dst)

    def __init__(self, base_dir, project_name):

        self.base_project_path = None
        self.config = None
        self.files = None

        try:

            self.base_project_path = os.path.join(base_dir, project_name);
            config_path = os.path.join(Initializer.ROOT_DIR, "resources", "config.json")

            try:
                with open(config_path, "r") as config:
                    self.config = json.load(config);
            except Exception as e:
                print("Failed to open config:")
                self.print_exception_info(e)

            Path(self.base_project_path).mkdir()
            self.make_dirs(self.base_project_path, self.config["dirs"])

            self.files = os.path.join(Initializer.ROOT_DIR, "resources", "files")
            self.copy_files(self.base_project_path, self.files, self.config["files"])
            
        except Exception as e:
            print(f'Error initializing')
            self.print_exception_info(e)