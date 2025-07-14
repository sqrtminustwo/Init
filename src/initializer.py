import os

class Initializer:

    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    def __init__(self, base_dir, project_name):
        self.path = None
        try:
            self.path = os.path.join(base_dir, project_name);
            to_create = []
            try:
                needed_dirs = os.path.join(Initializer.ROOT_DIR, "resources", "needed_dirs.txt");
                with open(needed_dirs, "r") as dirs:
                    to_create = [e.strip() for e in dirs.readlines()];
            except:
                print("Failed to open:", needed_dirs)

            for i in to_create:
                print(i)
        except:
            print(f'Invalid project name "{project_name}"', f'or directory {base_dir} where passed to initializer' if base_dir is not None else '');
        
