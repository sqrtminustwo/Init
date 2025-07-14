import initializer
import sys
import os

project_name = None
base_dir = os.getcwd()

try:
    project_name = sys.argv[1]
    if len(sys.argv) >= 3:
        try:
            base_dir = sys.argv[2]
        except:
            print('Invalid base dir')

    print(project_name, base_dir)
except:
    print('Usage: ./cppinit project_name [Base dir path]')

if (project_name is not None) or (base_dir is not None):
    init = initializer.Initializer(base_dir, project_name);
else:
    print(f'Invlaid project name {project_name} or base_dir {base_dir}')