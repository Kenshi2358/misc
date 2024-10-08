import inspect
import os
import sys
import zipfile

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(1, parent_dir)

# Local application imports
from settings import logger

directory1 = input('\nEnter the folder path of the zip files you want to unzip, rename, and re-zip:\n')

def unzip_files(dir_path):
    logger.info("Unzipping files")

    for each_file in os.listdir(dir_path):
        if each_file.endswith(".zip"):
            file_path = os.path.join(dir_path, each_file)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(dir_path)
            os.remove(file_path)


def rename_files(dir_path):
    logger.info("Renaming files")

    for each_file in os.listdir(dir_path):
        if not each_file.endswith(".zip") and not each_file.endswith(".ZIP"):
            base_name = each_file.split(".")[0]
            base_extension = each_file.split(".")[1]

            delta_pos = base_name.find("_DELTA_")
            if delta_pos >= 0:
                end_position = delta_pos + 7
                new_name = f"{base_name[:end_position]}TEST_{base_name[end_position:]}.{base_extension}"

                full_file_path = os.path.join(dir_path, each_file)
                new_file_path = os.path.join(dir_path, new_name)
                os.rename(full_file_path, new_file_path)


def zip_each_file(dir_path):
    logger.info("Rezipping files")

    for each_file in os.listdir(dir_path):
        if not each_file.endswith(".zip") and not each_file.endswith(".ZIP"):
            base_name = each_file.split(".")[0]
            new_name = f"{base_name}.ZIP"
            file_path = os.path.join(dir_path, each_file)
            zip_path = os.path.join(dir_path, new_name)
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
                zip_ref.write(file_path, each_file)
            os.remove(file_path)


unzip_files(directory1)
rename_files(directory1)
zip_each_file(directory1)
