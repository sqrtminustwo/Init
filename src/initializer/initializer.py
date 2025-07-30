import json
import shutil
import os
import sys
import traceback
import re
from re import Pattern
from pathlib import Path
from os import listdir
from os.path import isfile, join

class InitPart:
    def __init__(self, created_objects: list):
        self.created_objects = created_objects

    def extend(self, other: "InitPart") -> None:
        for obj in other.created_objects:
            self.created_objects.append(obj)

    def print_created(self) -> None:
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
    
    @staticmethod
    def append_path(path: str, append: list) -> str:
        for my_dir in append:
            path = os.path.join(path, my_dir)
        return path

    @staticmethod
    def get_files_in_dir(mydir: str) -> list:
        return [f for f in listdir(mydir) if isfile(join(mydir, f))]
    
    @staticmethod
    def get_matches_in_dir(files: list, regex: Pattern) -> list:
        return [f for f in files if regex.match(f)]
    
    def make_dirs(self, project_path: str, dirs: list) -> InitPart:
        created_dirs = []
        for dir_pack in dirs:
            path_temp = project_path
            for my_dir in dir_pack:
                path_temp = os.path.join(path_temp, my_dir)
                try:
                    Path(path_temp).mkdir()
                    created_dirs.append(path_temp)
                except:
                    pass
        return InitPart(created_dirs)

    def copy_files(self, project_path: str, files_path: str, config_files: list) -> InitPart:
        created_files = []
        for file in config_files:
            base_src = self.append_path(files_path, file["src_path"]) 
            avaliable_files = self.get_files_in_dir(base_src)

            toadd_names = None
            if "name" in file:
                toadd_names = self.get_matches_in_dir(avaliable_files, re.compile(file["name"]))
            else:
                toadd_names = [file["src_name"]]

            base_dst = self.append_path(project_path, file["dst_path"])

            for name in toadd_names:
                file_path_src = os.path.join(base_src, name)
                dst_name = name if "name" in file else file["dst_name"]
                file_path_dst = os.path.join(base_dst, dst_name)

                Path(file_path_dst).touch()
                shutil.copyfile(file_path_src, file_path_dst)
                created_files.append(file_path_dst)
        
        return InitPart(created_files)
    
    def load_project(self, config: dict) -> None:
            Path(self.base_project_path).mkdir()
            self.made_base_dir = True
            files = os.path.join(Initializer.ROOT_DIR, "resources", "files", config["files_root"])

            for section in config["structure"].values():
                if "dirs" in section:
                    self.created_dirs.extend(self.make_dirs(self.base_project_path, section["dirs"]))
                if "files" in section:
                    self.created_files.extend(self.copy_files(self.base_project_path, files, section["files"]))

            print("Made dirs:")
            self.created_dirs.print_created()
            print("Copied files:")
            self.created_files.print_created()
    
    def __init__(self, base_dir, project_name, config_name):

        if len(config_name) < 5 or not (re.compile("^.*\\.json$")).match(config_name):
            config_name += ".json"

        self.made_base_dir = False
        self.base_project_path = None
        self.created_dirs = InitPart([])
        self.created_files = InitPart([])

        try:
            self.base_project_path = os.path.join(base_dir, project_name);
            config_path = os.path.join(Initializer.ROOT_DIR, "resources", "configs", config_name)

            with open(config_path, "r", encoding="utf-8") as config:
                self.load_project(json.load(config));

        except Exception as ex:
            self.print_exception_info("Error initializing", ex)
            if self.made_base_dir:
                try:
                    shutil.rmtree(self.base_project_path)
                    print("Deleted base dir:")
                    print(self.base_project_path)
                except Exception as ex:
                    self.print_exception_info("Failed to delete base directory", ex)
            sys.exit()
