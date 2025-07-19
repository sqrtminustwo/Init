import json
import shutil
import os
import sys
import traceback
from pathlib import Path

class InitPart:
    def __init__(self, created_objects):
        self.created_objects = created_objects

    def print_created(self):
        for obj in self.created_objects:
            print(obj)

class Initializer:

    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    @staticmethod
    def print_exception_info(msg: str, ex: Exception) -> None:
        print(f'\n--- {msg} ---')
        print(f"Type    : {type(ex).__name__}")
        print(f"Message : {ex}")
        print("Traceback (most recent call last):")
        traceback.print_tb(ex.__traceback__)
        print("---------------------------\n")

    def __init__(self, base_dir, project_name, config_name):

        if len(config_name) < 5 or config_name[-5:] != ".json":
            config_name += ".json"

        self.base_project_path = None
        self.config = None
        self.files = None

        made_base_dir = False
        self.created_dirs = None
        self.created_files = None

        try:
            self.base_project_path = os.path.join(base_dir, project_name);
            config_path = os.path.join(Initializer.ROOT_DIR, "resources", "configs", config_name)

            try:
                with open(config_path, "r", encoding="utf-8") as config:
                    self.config = json.load(config);
            except Exception as ex:
                self.print_exception_info(f'Failed to open/read config "{config_name}"', ex)
                sys.exit()

            print("Loaded config:")
            print(config_path)

            Path(self.base_project_path).mkdir()
            made_base_dir = True
            self.created_dirs = self.make_dirs(self.base_project_path, self.config["dirs"])

            print("Made dirs:")
            self.created_dirs.print_created()

            self.files = os.path.join(Initializer.ROOT_DIR, "resources", "files", self.config["files_root"])
            self.created_files = self.copy_files(self.base_project_path, self.files, self.config["files"])

            print("Copied files:")
            self.created_files.print_created()

        except Exception as ex:
            self.print_exception_info("Error initializing", ex)
            if made_base_dir:
                try:
                    shutil.rmtree(self.base_project_path)
                    print("Deleted base dir:")
                    print(self.base_project_path)
                except Exception as ex:
                    self.print_exception_info("Failed to delete base directory", ex)
            sys.exit()

    def make_dirs(self, project_path: str, dirs: list) -> InitPart:
        created_dirs = []
        for my_dir in dirs:
            new_path = os.path.join(project_path, my_dir)
            Path(new_path).mkdir()
            created_dirs.append(new_path)
        return InitPart(created_dirs)

    def copy_files(self, project_path: str, files_path: str, config_files: list) -> InitPart:
        created_files = []
        for file in config_files:
            file_path_src = os.path.join(files_path, file["name"])
            file_path_dst = project_path

            for my_dir in file["path"]:
                file_path_dst = os.path.join(file_path_dst, my_dir)
            file_path_dst = os.path.join(file_path_dst, file["name"])

            Path(file_path_dst).touch()
            shutil.copyfile(file_path_src, file_path_dst)

            created_files.append(file_path_dst)
        return InitPart(created_files)