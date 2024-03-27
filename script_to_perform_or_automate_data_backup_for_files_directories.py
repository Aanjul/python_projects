# For refrence https://medium.com/@estebanpiero/10-useful-python-scripts-for-everyday-tasks-b0d74f2ea62c

import shutil

source_folder = '/path/to/source_folder'
backup_folder = '/path/to/backup_folder'

shutil.copytree(source_folder, backup_folder)