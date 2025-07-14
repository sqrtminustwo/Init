from initializer.initializer import Initializer
import sys
import os

project_name = None
base_dir = None

try:
    project_name = sys.argv[1]
    base_dir = os.getcwd()
except:
    print('Usage: ./cppinit project_name [Base dir path]')

if project_name is not None:
    init = Initializer(base_dir, project_name);
else:
    print(f'Invlaid project name {project_name} or base_dir {base_dir}')