from initializer.initializer import Initializer
import sys
import os

base_dir = None
config = None
project_name = None

try:
    base_dir = os.getcwd()
    config = sys.argv[1]
    project_name = sys.argv[2]
except:
    print('Usage: ./cppinit config project_name')
    sys.exit()

def print_if_none(arg, s: str) -> None:
    if arg is None:
        print(s)

if base_dir is not None and project_name is not None and config is not None:
    init = Initializer(base_dir, project_name, config);
else:
    print_if_none(base_dir, f'Invlaid base dir {base_dir};')
    print_if_none(project_name, f'Invlaid project name {project_name};')
    print_if_none(config, f'Invlaid config {config};')